"""Script to create vector DB for usage of RAG.

Reference:
  - [Document Loaders in LangChain]()
"""

import dotenv
from langchain.document_loaders.csv_loader import CSVLoader
from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import Chroma
from langchain_community.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import OpenAIEmbeddings


PERSISTENT_CHROMA_PATH = "chroma_data"
dotenv.load_dotenv()


def create_vector_db_of_repo(
    doc_paths: list[str], name='langchain_store'):
  embeddings = OpenAIEmbeddings(),
  # vectorstore = Chroma(
  #     name, embeddings, persist_directory=PERSISTENT_CHROMA_PATH)

  text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000, chunk_overlap=200)

  vectorstore = None
  for doc_path in doc_paths:
    loader = TextLoader(doc_path)
    splits = text_splitter.split_documents(loader.load())
    if vectorstore is None:
      vectorstore = Chroma.from_documents(
          documents=splits,
          embedding=OpenAIEmbeddings(),
          persist_directory=PERSISTENT_CHROMA_PATH)
    else:
      vectorstore.add_documents(splits)

  return vectorstore
