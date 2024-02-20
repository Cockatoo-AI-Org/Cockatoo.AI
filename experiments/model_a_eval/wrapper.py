"""Wrapper to incorporate exist model A package into pre-defined API interface.

Our evaluation of model A candidates is conducted using the pre-defined API
interfaces that is both accessible and easy to use. We define general-purpose
APIs here to guide the implementation of model A evaluation.
"""

import enum
from typing import Protocol


@enum.unique
class LangEnum(enum.Enum):
  en = 0
  cn = 1

  @classmethod
  def from_str(cls, lang_str: str):
    for supported_lang_enum in cls:
      if supported_lang_enum.name == lang_str:
        return supported_lang_enum

    raise ValueError(f'Unknown lang setting={lang_str}!')


class ModelA(Protocol):
  """Model A wrapper."""

  def __init__(self, lang: LangEnum = LangEnum.en):
    self.lang = lang

  @property
  def name(self) -> str:
    """Model/Approch name."""
    pass

  def audio_2_text(self, audio_file_path: str) -> str:
    """Turns audio of given file path into text.

    Args:
      audio_file_path: Audio file path to do audio to text transformation.

    Returns:
      Transformed speech text from given audio file.
    """
    pass


class ModelAMetric(Protocol):
  """Clz to calculate metric score of model A."""

  def score(
      self,
      transformed_text: str,
      ground_truth_text: str) -> float:
    """Calculates the metric score.

    Args:
      transformed_text: The text transformed by model A.
      ground_truth_text: The ground truth of text.

    Returns:
      The corresponding metric score.
    """
    pass
