"""Wrapper to incorporate exist model A package into pre-defined API interface.

Our evaluation of model A candidates is conducted using the pre-defined API
interfaces that is both accessible and easy to use. We define general-purpose
APIs here to guide the implementation of model A evaluation.
"""

from typing import Protocol


class ModelA(Protocol):
  """Model A wrapper."""

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
