"""Tools module used by all kinds of agents."""

import os
from dotenv import load_dotenv
from langchain.utilities import SerpAPIWrapper


class CustomSerpAPIWrapper(SerpAPIWrapper):
  def __init__(self):
    load_dotenv()
    super(CustomSerpAPIWrapper, self).__init__()

  @staticmethod
  def _process_response(res: dict) -> str:
    """Process response from SerpAPI."""
    if "error" in res.keys():
      raise ValueError(f"Got error from SerpAPI: {res['error']}")
    if "answer_box" in res.keys() and "answer" in res["answer_box"].keys():
      toret = res["answer_box"]["answer"]
    elif "answer_box" in res.keys() and "snippet" in res["answer_box"].keys():
      toret = res["answer_box"]["snippet"]
    elif (
      "answer_box" in res.keys()
      and "snippet_highlighted_words" in res["answer_box"].keys()
    ):
      toret = res["answer_box"]["snippet_highlighted_words"][0]
    elif (
      "sports_results" in res.keys()
      and "game_spotlight" in res["sports_results"].keys()
    ):
      toret = res["sports_results"]["game_spotlight"]
    elif (
      "knowledge_graph" in res.keys()
      and "description" in res["knowledge_graph"].keys()
    ):
      toret = res["knowledge_graph"]["description"]
    elif "snippet" in res["organic_results"][0].keys():
      toret = res["organic_results"][0]["link"]
    else:
      toret = "No good search result found"

    return toret


def search_2_cache_file(hash_value: str):
  return f"search_{hash_value}.txt"


def get_profile_url(name: str) -> str:
  """Searches for Linkedin profile page."""
  # https://serpapi.com/dashboard
  cache_txt_file = search_2_cache_file(hash(name))
  if os.path.isfile(cache_txt_file):
    print(f"Returning from cache file={cache_txt_file}...")
    with open(cache_txt_file, "r") as fo:
      return fo.read()

  search = CustomSerpAPIWrapper()
  res = search.run(f"{name}")

  print(f"Saving search result into {cache_txt_file}...")
  with open(cache_txt_file, "w") as fp:
    fp.write(res)

  return res
