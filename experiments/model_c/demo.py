"""
This file demos on how to call api.py for TTS models.
"""
from api import get_device, get_tts_model, record_voice


if __name__ == "__main__":

    # inputs that can parameterized via argparser in the future
    intput_text = "我想要吃飯，你有推薦的Restaurant嗎?"
    speaker = "Luis Moray"
    language = "zh-cn"
    file_path = "./output.wav"
    duration = 10
    speaker_wav = "./experiments/model_c/voice_ref/chung_recorded.wav"

    # retrieve model
    device = get_device()
    tts = get_tts_model(
        identifier="tts_models/multilingual/multi-dataset/xtts_v2"
    )
    print("list of available speakers:\n",
          tts.synthesizer.tts_model.speaker_manager.name_to_id
    )
    print("list of available languages:\n", tts.languages)

    # record voice (can be optional or conditional in the future)
    print("Please record your voice for references")
    _ = record_voice(duration=duration, file_path=speaker_wav)

    # inference
    # one of the spkear and speaker_wav (6-10 secs) must be given
    _ = tts.tts_to_file(
        intput_text, speaker=speaker, language=language, split_sentences=True,
        speaker_wav=speaker_wav, file_path=file_path
    )
