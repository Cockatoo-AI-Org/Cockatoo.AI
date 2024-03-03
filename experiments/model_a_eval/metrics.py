"""We defines interested metrics used for Model A here."""
import collections
import inspect
import logging
from nltk.tokenize import word_tokenize
import string
import sys
import wrapper


PUNCTUATION_MARK_SET = set(string.punctuation)


def cn_text_2_vector(text: str) -> list[str]:
  """Turns cn text into vector."""
  return [
      ch for ch in text
      if ch.strip() and ch.strip() not in PUNCTUATION_MARK_SET]


def en_text_2_vector(text: str, to_lower: bool = True) -> list[str]:
  """Turns en text into vector.

  Simple Usage:
  ```python
  >>> from metrics import *
  >>> text_2_vector('this is for testing. A quote word as "test".')
  ['this', 'is', 'for', 'testing', 'a', 'quote', 'word', 'as', 'test']
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


def get_default_metric() -> wrapper.ModelAMetric:
  """Gets default metric."""
  return WordErrorRateMetric


def get_all_metric() -> list[wrapper.ModelAMetric]:
  """Gets all supported metric."""
  supported_metric_list = []
  for clz_name, clz in inspect.getmembers(sys.modules[__name__]):
    if hasattr(clz, '__base__') and clz.__base__ == wrapper.ModelAMetric:
      supported_metric_list.append(clz)

  return supported_metric_list


def get_metric(metric_name: str) -> None | wrapper.ModelAMetric:
  """Gets metric according to its name."""
  for metric_clz in get_all_metric():
    if metric_clz.name == metric_name:
      return metric_clz

  return None


class JaccardSimMetric(wrapper.ModelAMetric):
  """Metric to calculate Jaccard simility.

  Jaccard Similarity also known as Jaccard index, is a statistic to measure the
  similarity between two data sets. It is measured as the size of the
  intersection of two sets divided by the size of their union.
  """

  name: str = 'jaccard_sim'

  def score(
      self,
      transformed_text: str,
      ground_truth_text: str) -> float:
    """Calculates the metric score."""
    if self.lang == wrapper.LangEnum.cn:
      text_2_vector = cn_text_2_vector
    else:
      text_2_vector = en_text_2_vector

    transformed_word_set = set(text_2_vector(transformed_text))
    ground_truth_word_set = set(text_2_vector(ground_truth_text))

    if len(transformed_word_set) == 0 and len(ground_truth_word_set) == 0:
      return 0.0

    inter_set = transformed_word_set.intersection(ground_truth_word_set)
    union_set = transformed_word_set.union(ground_truth_word_set)
    return len(inter_set) / len(union_set)


class WordErrorRateMetric(wrapper.ModelAMetric):
  """Word error rate metric.

  This is the most common metric used to evaluate ASR. Word error rate (WER)
  tells you how many words were logged incorrectly by the system during the
  conversation.

  The formula for calculating WER is: $WER = (S+D+I)/N$
  - **S = substitutions**: When the system captures a word, but it’s the wrong
      word. For example, it could capture “John was hoppy” instead of,
      “John was happy”.
  - **D = deletions**: These are words the system doesn’t include. Like,
      “John happy”.
  - **I = insertions**: When the system includes words that weren’t spoken,
      “John sure was happy”.
  - **N = total number of words spoken**: How many words are contained in the
      entire conversation.
  """

  name: str = 'wer'
  do_sort_reverse: bool = False

  def score(
      self,
      transformed_text: str,
      ground_truth_text: str) -> float:
    """Calculates the metric score."""
    if self.lang == wrapper.LangEnum.cn:
      text_2_vector = cn_text_2_vector
    else:
      text_2_vector = en_text_2_vector

    transformed_word_counter = collections.Counter(
        text_2_vector(transformed_text))
    ground_truth_word_counter = collections.Counter(
        text_2_vector(ground_truth_text))

    deletion_word_count = 0  # Stands for `D`
    insert_or_unknown_word_count = 0  # Stands for `S` + `I`
    total_word_count = (
        sum(map(lambda t: t[1], ground_truth_word_counter.items())))

    # Calculation of `D`
    for w, f in ground_truth_word_counter.items():
      deletion_word_count += (f - transformed_word_counter.get(w, 0))

    # Calculation of `S` + `I`
    for w, f in transformed_word_counter.items():
      if w not in ground_truth_word_counter:
        insert_or_unknown_word_count += f

    return (
        (deletion_word_count + insert_or_unknown_word_count)
        / total_word_count)
