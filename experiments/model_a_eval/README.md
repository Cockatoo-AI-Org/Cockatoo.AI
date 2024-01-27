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
+-------------------------+-----------------------+-------+----------+
|          Input          |          Name         | Score | Time (s) |
+-------------------------+-----------------------+-------+----------+
| en_20240108_johnlee.wav | SpeechRecognition/GCP |  1.0  |   4.69   |
| en_20240121_johnlee.wav | SpeechRecognition/GCP |  1.0  |   1.65   |
|  en_20240121_chung.wav  | SpeechRecognition/GCP |  0.81 |  10.13   |
+-------------------------+-----------------------+-------+----------+
```