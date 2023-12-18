# Project language tutor (focused on listening & speaking)

_In the Open issues, please put your name at the end of the task that you are interested in._

# Goal towards users:
- Speak as native as possible to users so users can practice listening as well as speaking.
- Can adjust the language tutor’s teaching attitude (e.g., Direct vs Plato)
- Can adjust the language tutor’s speaking/work usage difficulties (e.g., A1, A2, B1, B2, C1 levels) to make learning easier for users.
- Can discuss the topic the user uploaded/raised and can correspondingly ask appropriate questions to the user. 
- Can practice listening to various tones from AI (e.g., expressing the sentence with happiness, sadness, …, from elderly/adult/woman/man …)

# Goal towards team members:
- Improve LLM, voice models, DL, and other framework knowledge/skills. 
- Can use the language tutor to benefit him/herself.
- Learn CI/CD and do research on improving potential product biasedness and relevant skills. 
- Learn the balance between fine-tuning and our computing powers.

# How To (Initiative):
Use models (A-B-C as shown below) to form the pipeline as the final language tutor:
- model A: voice to text
- model B(LLM): text à text , might be managed by [langChain](https://python.langchain.com/docs/get_started/introduction), Andrew Ng provided [2-3 free short courses](https://www.deeplearning.ai/short-courses/).
- model C: text to voice
PS: C might be the same as A, needs more research. But the** Goal towards users** should be the top concern when considering which model to use. Besides, better to use open-source models instead of paying premium APIs.

For model C, one may use LangChain to manage LLM. langChain is a tool that helps build automation pipelines, store vector databases (our own data), and automate the monitoring of LLM with various technical strategies as well as prompt engineering. For example, we may manage the prompt strategy by telling LLM to self-supervise the output text quality, ie, tell LLM to redo it again if the previous output was not good.


# Market Competitors (for language tutoring)
- Langotalk (multi-lan)
- Tutor Lily: AI Language Tutor (multi-lan)

# Good References
## For Model A (Speech to text, STT)
- The library [`SpeechRecognition`](https://pypi.org/project/SpeechRecognition/)
  is used for performing speech recognition, with support for several engines and APIs, online and offline.
    - [Notebook - Easy Speech-to-Text with Python](https://github.com/johnklee/ml_articles/blob/master/medium/Easy-speech-to-text-with-python/notebook.ipynb)
## For Model C (Text to speech, TTS)
- The company [Evelenlabs](https://elevenlabs.io/) has advanced **non-open sourced** TTS model for multi-languages. It performs well in Chinese (no Taiwanese tone) and English from my perspective, which inlcudes happy/sad/... tones as well as male/female/... sounds.


# Misc
