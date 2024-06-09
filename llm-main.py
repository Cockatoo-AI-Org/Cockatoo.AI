# llm-backend/llm-main.py
# Author: Louis Chang
# DESCRIPTION: This file contains the implementation of the backend for LLM settings and chat.
# Version 0.3 - 2024/06/09

# - Version 0.1 - 2024/06/02: Create the backend.
# - Version 0.2 - 2024/06/09: Add the functionality to adjust model settings.
# - Version 0.3 - 2024/06/16: Add the functionality to select the model & some preview func for RAG & LangChain.

from fastapi import FastAPI, Request, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from transformers import AutoTokenizer, pipeline
import torch
import langchain

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all HTTP headers
)

settings = {
    "model": "google/gemma-7b-it",
    "max_new_tokens": 2056,
    "do_sample": True,
    "temperature": 0.9,
}

def load_model(model_name):
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    chat_pipeline = pipeline(
        "text-generation",
        model=model_name,
        model_kwargs={"torch_dtype": torch.bfloat16},
        device=0 if torch.cuda.is_available() else -1,  # Set device based on CUDA availability
    )
    return tokenizer, chat_pipeline

tokenizer, chat_pipeline = load_model(settings["model"])

@app.post("/settings")
async def update_settings(request: Request):
    new_settings = await request.json()
    settings.update(new_settings)
    
    # Reload the model
    global tokenizer, chat_pipeline
    tokenizer, chat_pipeline = load_model(settings["model"])
    
    return {"message": "Settings updated successfully"}

@app.post("/chat")
async def chat(request: Request):
    data = await request.json()
    user_input = data['message']
    messages = [
        {"role": "user", "content": user_input},
    ]
    prompt = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
    outputs = chat_pipeline(
        prompt,
        max_new_tokens=settings["max_new_tokens"],
        do_sample=settings["do_sample"],
        temperature=settings["temperature"],
    )
    generated_text = outputs[0]['generated_text']
    reply = generated_text[len(prompt):]
    return {"reply": reply}

@app.post("/upload")
async def upload(file: UploadFile = File(...)):
    # Save the file and handle it accordingly
    return {"filename": file.filename}

@app.post("/search")
async def search(request: Request):
    data = await request.json()
    query = data['query']
    # Use Langchain to connect to a specific URL and perform RAG
    results = langchain.search(query)
    return {"results": results}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
