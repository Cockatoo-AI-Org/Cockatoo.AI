"""
tts package supports using command line or python to call model for training
or inferencing. Here we deomnstrate how to use python to call models
"""
from typing import Optional, TypeAlias
import sounddevice as sd
from scipy.io import wavfile
import torch
from TTS.api import TTS

DeviceLikeType: TypeAlias = str | torch.device | int


def get_device() -> str:
    """Check if cuda is available and return corresp. string"""
    device = "cuda" if torch.cuda.is_available() else "cpu"
    return device


def get_tts_model(
    identifier: Optional[str] = None, device: DeviceLikeType = "cpu"
) -> TTS:
    """
    Get specified TTS model via input ``identifier`` string. The avaiable
    identifiers can be found via ``TTS().list_models().list_models()``.

    Parameters
    ----------
    identifier: str
        supported model name of format <model_category> / <language_code> /
        <voice_or_dataset_category> / <model_name>. For more details, please
        check with the code ``TTS().list_models().list_models()``.
        Defaults to "tts_models/multilingual/multi-dataset/xtts_v2" if None.
    device: DeviceLikeType, optional
        Can be str, torch.device type, or int to indicate desired device for
        usage. For example, cpu, cuda, 0, or 'cuda:0' etc. Defaults to 'cpu'.
    
    Returns
    -------
    TTS
        Returned model of type TTS.
    """
    # Notice that XTTSv2 has license for non-commerical use only.
    identifier = identifier or "tts_models/multilingual/multi-dataset/xtts_v2"
    return TTS(identifier).to(device)


def record_voice(
    duration: int | float = 6, rate: int = 44100, file_path: str = "record.wav"
) -> str:
    """
    Record user voice as reference for model C, if the voice cloning is
    supported by the choosen model.

    .. note::
      The function currently only records a fixed amount of time via ``duration``,
      this can be improved by steramline recording until the user press a key
      to stop it. More info: `Sounddevice Example`_.

    .. _Sounddevice Example: https://python-sounddevice.readthedocs.io/en/0.4.5/examples.html#recording-with-arbitrary-duration

    Parameters
    ----------
    duration : int | float, optional
        duration of recording (in seconds), by default 6
    rate : int, optional
        the same rate (in samples/sec), by default 44100.
    file_path: str, optional
        output path for recording, by default "record.wav".

    Returns
    -------
    str
       file_path (same as the input arg).
    """
    recording = sd.rec(frames=int(duration * rate), samplerate=rate, channels=2)
    sd.wait()  # wait until recording is finished
    wavfile.write(file_path, rate, recording)
    return file_path
