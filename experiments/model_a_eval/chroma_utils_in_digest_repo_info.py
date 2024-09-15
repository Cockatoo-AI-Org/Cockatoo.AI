#!/bin/env python
"""Utility to digest knowledge/information of current repo as vectorstore."""
import os
import sys
import pathlib
import chromadb
from chromadb.utils import embedding_functions
from langchain_openai import OpenAIEmbeddings
from more_itertools import batched
from dotenv import load_dotenv
import openai


# Please prepare a .env file to hold below setting:
# OPENAI_API_KEY=xxx
load_dotenv()
openai.api_key = os.environ['OPENAI_API_KEY']


TEST_DOC_PATHS = [
    'README.md', '../../README.md', '../model_c/README.md',
    '../langchain_lab/README.md', '../../docs/README.md']
CHROMA_PATH = "cockatoo_repo_embeddings"
EMBEDDING_FUNC_NAME = "multi-qa-MiniLM-L6-cos-v1"
COLLECTION_NAME = "cockatoo_knowledge"


def text_embedding(embedding_obj, text):
    embedding_obj.create(model="text-embedding-ada-002", input=text)
    return response["data"][0]["embedding"]


def prepare_chroma_data(file_path_list: list[str]):
  """Prepare the car reviews dataset for ChromaDB"""
  ids = []
  documents = []
  metadatas = []
  for id_num, file_path in enumerate(file_path_list, 1):
    ids.append(str(id_num))
    document_content = open(file_path).read()
    documents.append(document_content)
    metadata = {
        'file_path': file_path,
        'dir': os.path.abspath(os.path.dirname(file_path))}
    metadatas.append(metadata)

  # Create ids, documents, and metadatas data in the format chromadb expects
  print(f'Total {len(documents)} documents collected!')
  return {"ids": ids, "documents": documents, "metadatas": metadatas}


def build_chroma_collection(
    chroma_path: pathlib.Path,
    collection_name: str,
    embedding_func_name: str,
    ids: list[str],
    documents: list[str],
    metadatas: list[dict],
    distance_func_name: str = "cosine"):
  """Create a ChromaDB collection"""
  chroma_client = chromadb.PersistentClient(chroma_path)

  openai_ef = embedding_functions.OpenAIEmbeddingFunction(
      model_name="text-embedding-ada-002")

  # embedding_func = embedding_functions.SentenceTransformerEmbeddingFunction(
  #     model_name=embedding_func_name)
  # embeddings = OpenAIEmbeddings()

  collection = chroma_client.create_collection(
      name=collection_name,
      # embedding_function=embedding_func,
      embedding_function=openai_ef,
      metadata={"hnsw:space": distance_func_name})

  document_indices = list(range(len(documents)))

  collection.add(
    ids=ids,
    documents=documents,
    metadatas=metadatas)

  return collection


if __name__ == '__main__':
  test_chroma_dataset = prepare_chroma_data(TEST_DOC_PATHS)
  build_chroma_collection(
    CHROMA_PATH,
    COLLECTION_NAME,
    EMBEDDING_FUNC_NAME,
    test_chroma_dataset["ids"],
    test_chroma_dataset["documents"],
    test_chroma_dataset["metadatas"])
