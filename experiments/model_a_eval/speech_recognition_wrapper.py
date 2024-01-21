"""Wrapper of package `speech_recognition`."""
import dataclasses
import logging
import speech_recognition as sr
import time
import wrapper


@dataclasses.dataclass
class Audio2TextData:
  text: str
  spent_time_sec: float


class SRGoogleWrapper(wrapper.ModelA):
  """Wrapper of speech_recognition.Recognizer.

  For this version, it will delegate the operation to Google Cloud Speech API:
  - https://cloud.google.com/speech-to-text?hl=zh_tw
  """
  
  def __init__(self):
    self._speech_recognizer = sr.Recognizer()

  @property
  def name(self) -> str:
    return 'SpeechRecognition/GCP'

  def audio_2_text(self, audio_file_path: str) -> str:
    start_time = time.time()
    with sr.AudioFile(audio_file_path) as source:   
      try: 
        # using google speech recognition
        audio_text = self._speech_recognizer.listen(source)
        text = self._speech_recognizer.recognize_google(audio_text)
        time_diff_sec = time.time() - start_time
        return Audio2TextData(
            text=text, spent_time_sec=time_diff_sec)
      except sr.exceptions.UnknownValueError as ex:
        logging.warning(
            f'Can not transform the input audio file from {audio_file_path}')
        time_diff_sec = time.time() - start_time
        return Audio2TextData(
            text='', spent_time_sec=time_diff_sec)
      except Exception as ex:
        logging.error(
            f'Failed to transform audio to text from {audio_file_path}')
        raise ex
