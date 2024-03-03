## Evaluation of Model A
Here will hold the instructions on how to do evaluation on Model A (STT).

## Prepare audio files and ground truth text files.
First step is to collect audio files and the expected text as ground truth for
Model A to extract from. The audio files and text files should have same names
for the framework to process. e.g.:
```shell
# ls -hl
total 3.8M
-rw-r--r-- 1 root root  110 Jan  8 09:38 en_20240108_johnlee.txt
-rw-rw-r-- 1 john john 2.5M Jan 21 16:40 en_20240108_johnlee.wav
...
```

Next, we use environment variable `AUDIO_DATA_ROOT_SRC_PATH` to point to your data root path:
```shell
$ export AUDIO_DATA_ROOT_SRC_PATH=<Path to the folder where holds the ground truth files>
```

## Install the necessary Python packages
Please execute below command to install necessary Python packages:
```shell
$ pip install -r requirements.txt
```

## Execute the evaluation
Execute below command to run the evaluation:
```shell
$ ./eval.py
...
Raw data (LangEnum.en)
+-------------------------+------------------------------+-------+----------+
|          Input          |             Name             | Score | Time (s) |
+-------------------------+------------------------------+-------+----------+
| en_20240108_johnlee.wav |    SpeechRecognition/GCP     |  1.0  |   3.95   |
| en_20240108_johnlee.wav | SpeechRecognition/WhisperAPI |  1.0  |   3.26   |
| en_20240121_johnlee.wav |    SpeechRecognition/GCP     |  1.0  |   1.69   |
| en_20240121_johnlee.wav | SpeechRecognition/WhisperAPI |  1.0  |   1.6    |
|  en_20240121_chung.wav  |    SpeechRecognition/GCP     |  0.81 |   8.49   |
|  en_20240121_chung.wav  | SpeechRecognition/WhisperAPI |  0.87 |   3.39   |
+-------------------------+------------------------------+-------+----------+

Ranking Table
+------------------------------+------------+--------------+
|             Name             | Avg. score | Avg. Time(s) |
+------------------------------+------------+--------------+
| SpeechRecognition/WhisperAPI |    0.96    |     2.75     |
|    SpeechRecognition/GCP     |    0.94    |     4.71     |
+------------------------------+------------+--------------+
```

### Switch to different language
We could use argument `--lang` or `-l` to switch the language we want to evaluate. e.g.:
```shell
# ./eval.py  --lang=cn
...
Raw data (LangEnum.cn)
+-------------------------+------------------------------+-------+----------+
|          Input          |             Name             | Score | Time (s) |
+-------------------------+------------------------------+-------+----------+
| cn_20240108_johnlee.wav |    SpeechRecognition/GCP     |  0.36 |   5.44   |
| cn_20240108_johnlee.wav | SpeechRecognition/WhisperAPI |  0.88 |   2.58   |
|  cn_20240121_chung.wav  |    SpeechRecognition/GCP     |  0.93 |  14.66   |
|  cn_20240121_chung.wav  | SpeechRecognition/WhisperAPI |  0.96 |   3.0    |
+-------------------------+------------------------------+-------+----------+

Ranking Table
+------------------------------+------------+--------------+
|             Name             | Avg. score | Avg. Time(s) |
+------------------------------+------------+--------------+
| SpeechRecognition/WhisperAPI |    0.92    |     2.79     |
|    SpeechRecognition/GCP     |    0.65    |    10.05     |
+------------------------------+------------+--------------+
```

### Switch to different metric
We could use argument `--metric` or `-m` to switch the metric for evaluation.
e.g.:
```shell
$ ./eval.py -m=jaccard_sim
...
Raw data (LangEnum.en)
+-------------------------+------------------------------+-------+----------+
|          Input          |             Name             | Score | Time (s) |
+-------------------------+------------------------------+-------+----------+
| en_20240121_johnlee.wav |    SpeechRecognition/GCP     |  1.0  |   1.04   |
| en_20240121_johnlee.wav | SpeechRecognition/WhisperAPI |  1.0  |   2.06   |
|  en_20240121_chung.wav  |    SpeechRecognition/GCP     |  0.81 |   8.1    |
|  en_20240121_chung.wav  | SpeechRecognition/WhisperAPI |  0.87 |   1.88   |
+-------------------------+------------------------------+-------+----------+

Ranking Table (metric=<class 'metrics.JaccardSimMetric'>)
+------------------------------+------------+--------------+
|             Name             | Avg. score | Avg. Time(s) |
+------------------------------+------------+--------------+
| SpeechRecognition/WhisperAPI |    0.93    |     1.97     |
|    SpeechRecognition/GCP     |    0.9     |     4.57     |
+------------------------------+------------+--------------+
```


## FAQ

### openai.error.RateLimitError: Rate limit reached for whisper-1
Please try again in 20s. Visit https://platform.openai.com/account/rate-limits to learn more. You can increase your rate limit by adding a payment method to your account at https://platform.openai.com/account/billing.
