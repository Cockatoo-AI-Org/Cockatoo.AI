from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained("google/gemma-2b")
model = AutoModelForCausalLM.from_pretrained("google/gemma-2b")

input_text = "Write me a python code to expand the C/C++ for loop & if-else / while...etc statement."
input_ids = tokenizer(input_text, return_tensors="pt")

outputs = model.generate(**input_ids, max_new_tokens=200)
print(tokenizer.decode(outputs[0]))

# Prompt format
# The base models have no prompt format. Like other base models, they can be used to continue an input sequence with a plausible continuation or for zero-shot/few-shot inference. They are also a great foundation for fine-tuning on your own use cases. The Instruct versions have a very simple conversation structure:

# <start_of_turn>user
# knock knock<end_of_turn>
# <start_of_turn>model
# who is there<end_of_turn>
# <start_of_turn>user
# LaMDA<end_of_turn>
# <start_of_turn>model
# LaMDA who?<end_of_turn>

# This format has to be exactly reproduced for effective use. We’ll later show how easy it is to reproduce the instruct prompt with the chat template available in transformers.