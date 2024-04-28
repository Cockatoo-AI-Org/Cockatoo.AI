## Langchain - Leverage agent to query information from Google

This section demonstrates how LangChain utilizes agents to query Google for
information it lacks and then extract the relevant parts to answer the question.
To try the sample code below, you'll need to complete some preparation steps.

### Prerequisite

* Please go to register or login https://serpapi.com/dashboard to retrieve API
  key and save it as environment variable `SERPAPI_API_KEY` in file `.env`
* Pleae go to register or login https://platform.openai.com/api-keys to retrieve
  API key and save it as environment variable `OPENAI_API_KEY` in file `.env`
* Create a virtual python runtime environment and install necessary packages:

```shell
$ virtualenv env
$ source env/bin/active
(env) $ pip install -r requirements.txt
...
```

## Sample Code
For below sample codes to work properly, please prepare a `.env` file to hold
below variables which will be referred from source code:
* **`OPENAI_API_KEY`**: OpenAI API key. (https://platform.openai.com/api-keys)
* **`SERPAPI_API_KEY`**: Your unique access key for authenticating with the [SerpApi service](https://serper.dev/).

### Demonstrate the usage of Agent
Please follow below instructions to query the Linkedin URL of people with
searching string as "Google Test Engineer Lee John":
```python
>>> from agents.linkedin_lookup_agent import lookup
>>> lookup('Google Test Engineer Lee John')
...
> Entering new AgentExecutor chain...
I should use the tool to crawl Google for the Linkedin profile page of Google Test Engineer Lee John.
Action: Crawl Google for linkedin profile page
Action Input: Google Test Engineer Lee John LinkedinSaving search result into search_5066441651125638471.txt...

Observation: https://tw.linkedin.com/in/lee-john-81601a7a
Thought:I now know the final answer
Final Answer: https://tw.linkedin.com/in/lee-john-81601a7a

> Finished chain.
'https://tw.linkedin.com/in/lee-john-81601a7a'
```

The final result is `https://tw.linkedin.com/in/lee-john-81601a7a` which is
correct as my Linkedin URL.

### Demonstrate the usage of RAG
This section will demonstrate the usage of [RAG](https://www.promptingguide.ai/techniques/rag) (a.k.a Retrieval Augmented
Generation). For RAG to work, the first step is to create the vector store which
will be used as reference for LLM to answer question:
```python
>>> from scripts import doc_loader
>>> doc_path = '...'  # Please replace `...` with doc path we want LLM to search for.
>>> vectorstore = doc_loader.create_vector_db_of_repo([doc_path])
```

Then we could test the vectorstore with question to retrieve the releveant docs:
```python
>>> question = 'Where do we put the sample code of LangChain?'
>>> relevant_docs = vectorstore.similarity_search(question, k=3)
>>> print(relevant_docs[0].page_content)
...
* `src/`: store source codes mainly .py files.
* `experiments/`: store experiment files. I created an empty .ipynb file to keep Git able to detect and upload the folder.
  - `experiments/langchain_lab/`: We put the sample codes of [`LangChain`](https://python.langchain.com/docs/get_started/introduction) here.
  - `experiments/model_a_eval/`: We put the code/framework to evaluate model A
    here.
...
```

Finally, we could provide our LLM chatbot with this `vectorstore` and query it:
```python
>>> from chatbot_demo import rag
>>> rag_chatbot = rag.get_chatbot(vectorstore)
>>> rag_chatbot.invoke(question)
'The sample codes of LangChain should be placed in the `experiments/langchain_lab/` directory within the `Cockatoo.AI` repository. This directory is specifically designated for storing the sample codes of LangChain.'
```
