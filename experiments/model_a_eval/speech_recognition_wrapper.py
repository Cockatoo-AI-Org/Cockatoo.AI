"""Wrapper of package `speech_recognition`."""
import dataclasses
import logging
from openai import OpenAI
import os
import time
import wrapper


@dataclasses.dataclass
class Audio2TextData:
  text: str
  spent_time_sec: float


class SRWhisperWrapper(wrapper.ModelA):
  """Wrapper of speech_recognition.Recognizer (for Whisper API users)."""

  def __init__(self, lang: wrapper.LangEnum):
    super().__init__(lang)
    self._client = OpenAI()

  @property
  def name(self) -> str:
    return 'SpeechRecognition/WhisperAPI'

  def audio_2_text(self, audio_file_path: str) -> str:
    audio_file_path = os.path.expanduser(audio_file_path)
    start_time = time.time()
    try:
      # Using Whisper API
      transcription = self._client.audio.transcriptions.create(
          model="whisper-1",
        file=open(audio_file_path, 'rb'))

      audio_text = transcription.text
      time_diff_sec = time.time() - start_time
      return Audio2TextData(
          text=audio_text, spent_time_sec=time_diff_sec)
    except Exception as ex:
      logging.error(
          f'Failed to transform audio to text from {audio_file_path}')
      raise ex


class SRGoogleWrapper(wrapper.ModelA):
  """Wrapper of speech_recognition.Recognizer.

  For this version, it will delegate the operation to Google Cloud Speech API:
  - https://cloud.google.com/speech-to-text?hl=zh_tw
  - https://cloud.google.com/speech-to-text/docs/speech-to-text-supported-languages
  """

  def __init__(self, lang: wrapper.LangEnum):
    super().__init__(lang)
    self.language = 'en-US'
    if lang == wrapper.LangEnum.cn:
      self.language = 'zh-TW'

    self._speech_recognizer = sr.Recognizer()

  @property
  def name(self) -> str:
    return 'SpeechRecognition/GCP'

  def audio_2_text(self, audio_file_path: str) -> str:
    audio_file_path = os.path.expanduser(audio_file_path)
    start_time = time.time()
    with sr.AudioFile(audio_file_path) as source:
      try:
        # using google speech recognition
        audio_text = self._speech_recognizer.listen(source)
        text = self._speech_recognizer.recognize_google(
            audio_text, language=self.language)
        time_diff_sec = time.time() - start_time
        return Audio2TextData(
            text=text, spent_time_sec=time_diff_sec)
      except sr.exceptions.UnknownValueError:
        logging.warning(
            f'Can not transform the input audio file from {audio_file_path}')
        time_diff_sec = time.time() - start_time
        return Audio2TextData(
            text='', spent_time_sec=time_diff_sec)
      except Exception as ex:
        logging.error(
            f'Failed to transform audio to text from {audio_file_path}')
        raise ex
