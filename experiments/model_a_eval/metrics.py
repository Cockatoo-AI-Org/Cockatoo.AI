"""We defines interested metrics used for Model A here."""
import logging
from nltk.tokenize import word_tokenize
import string
from typing import List
import wrapper


def text_2_vector(text: str, to_lower: bool = True) -> List[str]:
  """Turns text into vector.

  Simple Usage:
  ```python
  >>> from metrics import *
  >>> text_2_vector('this is for testing. How interesting! A quote word as "test".')
  ['this', 'is', 'for', 'testing', 'how', 'interesting', 'a', 'quote', 'word', 'as', 'test']
  ```
  """
  words = word_tokenize(text)
  logging.info('text to words: %s', words)
  # Remove punctuation
  words = list(filter(
      lambda w: w not in string.punctuation, words))
  logging.info('words without punct: %s', words)

  # Remove not-alphanumeric
  words = list(filter(
      lambda w: w.isalnum(), words))

  # Lower the words
  if to_lower:
    words = list(map(lambda w: w.lower(), words))

  return words


class JaccardSimMetric(wrapper.ModelAMetric):
  """Metric to calculate Jaccard simility.

  Jaccard Similarity also known as Jaccard index, is a statistic to measure the
  similarity between two data sets. It is measured as the size of the
  intersection of two sets divided by the size of their union.
  """

  def score(
      self,
      transformed_text: str, ground_truth_text: str) -> float:
    """Calculates the metric score."""
    transformed_word_set = set(text_2_vector(transformed_text))
    ground_truth_word_set = set(text_2_vector(ground_truth_text))

    if len(transformed_word_set) == 0 and len(ground_truth_word_set) == 0:
      return 0.0

    inter_set = transformed_word_set.intersection(ground_truth_word_set)
    union_set = transformed_word_set.union(ground_truth_word_set)
    return len(inter_set) / len(union_set)
