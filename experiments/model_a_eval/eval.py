#!/usr/bin/env python
import os
from metrics import *
from pathlib import Path
from prettytable import PrettyTable
from speech_recognition_wrapper import *


AUDIO_DATA_ROOT_SRC_PATH = os.environ.get(
    'AUDIO_DATA_ROOT_SRC_PATH', '/tmp/')


if __name__ == '__main__':
  sr_wrapper = SRGoogleWrapper()
  metric = JaccardSimMetric()
  score_table = PrettyTable(['Input', 'Name', 'Score', 'Time (s)'])
  for wav_file in filter(
      lambda f: f.endswith('.wav'),
      os.listdir(AUDIO_DATA_ROOT_SRC_PATH)):
    print(f'=== Processing {wav_file} ===')
    ground_truth_file_path = os.path.join(
        AUDIO_DATA_ROOT_SRC_PATH, f'{Path(wav_file).stem}.txt')
    if not os.path.isfile(ground_truth_file_path):
      raise Exception(
      f'Ground truth text file does not exist! ({ground_truth_file_path})')
    wav_file_path = os.path.join(AUDIO_DATA_ROOT_SRC_PATH, wav_file)

    with open(ground_truth_file_path, 'r') as fo:
      ground_truth_text = fo.read()

    print(f'Ground truth text: {ground_truth_text}')
    a2t_data = sr_wrapper.audio_2_text(wav_file_path)
    print(f'Transformed text: {a2t_data.text}')
    score = metric.score(a2t_data.text, ground_truth_text)
    score_table.add_row(
        [wav_file, sr_wrapper.name, round(score, 2), round(a2t_data.spent_time_sec, 2)])
    print('')

  print(score_table)
  print('')
