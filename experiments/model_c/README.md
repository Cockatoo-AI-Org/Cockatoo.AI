# Text to Speech (TTS) model notes

## General: 
 - [TTS Intro](https://huggingface.co/docs/transformers/tasks/text-to-speech)
 - [What is TTS](https://huggingface.co/tasks/text-to-speech) (Suno Bark, MS SpeechT5, MMS TTS)


## Resources

### Open AI TTS API
 - Pricing:
   Model | Usage 
   -- | -- 
   Whisper | $0.006 / minute (rounded to the nearest second)
   TTS | $0.015 / 1K characters
   TTS HD | $0.030 / 1K characters
 - [API Tutorial](https://platform.openai.com/docs/guides/text-to-speech)

### [Speech-T5-TTS](https://huggingface.co/microsoft/speecht5_tts)
 - [Interactive Demo](https://huggingface.co/spaces/Zhenhong/text-to-speech-SpeechT5-demo): only support for English, and the generated sound is too monotonic without cadence.
 - Currently the English TTS are good for most models that I have tried. The problem is that when it comes to Chinese-English mixed text, it is hard for model to synthesize the output voice

### [Suno Bark Github](https://github.com/suno-ai/bark)
Suno Bark model is also supported in Coqui TTS, or in Hugging Face Framework.
 - [Tutorial](https://huggingface.co/suno/bark)
 - [Bark Docs](https://huggingface.co/docs/transformers/main/en/model_doc/bark)
 - Bark supported preset voices: [Bark Speaker Library v2](https://suno-ai.notion.site/8b8e8749ed514b0cbf3f699013548683?v=bc67cff786b04b50b3ceb756fd05f68c). It supports multi-language, including simplified Chinese, but not Taiwanese tones. Users can click this speaker library to listen to some demos there (for me the generated quality is so so). 
 - [Interactive Demo](https://huggingface.co/spaces/suno/bark): users can interact with Bark model.

### [Coqui Github](https://github.com/coqui-ai/TTS)
- [Interactive Demo](https://huggingface.co/spaces/coqui/xtts)
- Allows user to input voice and text so model can imitate your voice to speak out the texts.


## Evaluations
In the world of TTS models, there are three or more evalution methods (keep updating...):
- Log F0
- Human eval in the loop
- mel cepstral distortion (MCD)


## Notes
At the end, I wanna record some technical terms encountered when reading papers so as to easy recall them in the future:
- Speaker Verification
- (log-)mel Spectrogram
