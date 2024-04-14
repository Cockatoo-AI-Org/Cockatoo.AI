"""Samples of Chatbot."""
import dotenv
from langchain.prompts import (
    PromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
    ChatPromptTemplate,
)
from langchain.schema.runnable import RunnablePassthrough
from langchain_community.chat_models import ChatOpenAI
from langchain_community.vectorstores import Chroma
from langchain_core.output_parsers import StrOutputParser

import textwrap


# Below variables are required in current module:
# - OPENAI_API_KEY: OpenAI API key. (https://platform.openai.com/api-keys)
dotenv.load_dotenv()


def get_chatbot(
    vectorstore, most_relevant_doc_count: int = 10):
  """Gets Chatbot.

  Args:
    vectorstore: Vectorscore for RAG chatbot to query the reference.
    most_relevant_doc_count: The maximum number of documents to retrieve from
      the vectorstore (default: 10)

  Returns:
    Chatbot object.
  """
  qa_system_template_str = textwrap.dedent("""
  Your job is to play senior engineer
  to answer questions about how to use the repo `Cockatoo.AI` on Github.

  Use the following context to answer questions. Be as detailed as possible,
  but don't make up any information that's not from the context.

  If you don't know an answer, say you don't know.

  {context}
  """).strip()

  review_system_prompt = SystemMessagePromptTemplate(
      prompt=PromptTemplate(
          input_variables=["context"], template=qa_system_template_str
      )
  )

  review_human_prompt = HumanMessagePromptTemplate(
      prompt=PromptTemplate(
          input_variables=["question"], template="{question}"
      )
  )

  messages = [review_system_prompt, review_human_prompt]
  review_prompt_template = ChatPromptTemplate(
      input_variables=["context", "question"],
      messages=messages,
  )

  chat_model = ChatOpenAI(model="gpt-3.5-turbo-0125", temperature=0)
  retriever = vectorstore.as_retriever(k=most_relevant_doc_count)
  qa_chain_with_rag = (
      {"context": retriever, "question": RunnablePassthrough()}
      | review_prompt_template
      | chat_model
      | StrOutputParser()
  )
  return qa_chain_with_rag
