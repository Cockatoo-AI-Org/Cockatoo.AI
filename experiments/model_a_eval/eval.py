#!/usr/bin/env python
import argparse
import constants
import os
import logging
import re
from collections import defaultdict
import metrics
from pathlib import Path
from prettytable import PrettyTable
from speech_recognition_wrapper import SRGoogleWrapper
from speech_recognition_wrapper import SRWhisperWrapper
import wrapper


Color = constants.Color
AUDIO_DATA_ROOT_SRC_PATH = os.environ.get(
    'AUDIO_DATA_ROOT_SRC_PATH', '/tmp/')


if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument(
      '--lang', '-l',
      help='language you would like to evaluate.',
      choices=['en', 'cn'],
      default='en',
      type=str)
  parser.add_argument(
      '--metric', '-m',
      help='Metric you would like to use.',
      choices=list(map(lambda m: m.name, metrics.get_all_metric())),
      default=metrics.get_default_metric().name,
      type=str)
  args = parser.parse_args()

  lang_setting = wrapper.LangEnum.from_str(args.lang)
  logging.info('setting lang=%s', lang_setting)

  wav_file_name_pattern = re.compile(lang_setting.name + r'_\d{8}_.*[.]wav')
  model_a_list = [
    SRGoogleWrapper(lang=lang_setting),
    SRWhisperWrapper(lang=lang_setting),
  ]

  metric_clz = metrics.get_metric(args.metric)
  metric = metric_clz(lang=lang_setting)
  # Key as model name; value as accumulated score.
  model_accumulated_scores = defaultdict(list)
  model_accumulated_time = defaultdict(list)
  score_table = PrettyTable(['Input', 'Name', 'Score', 'Time (s)'])
  for wav_file in filter(
      lambda f: wav_file_name_pattern.match(f),
      os.listdir(AUDIO_DATA_ROOT_SRC_PATH)):
    print(f'{Color.BOLD}=== Processing {wav_file} ==={Color.END}')
    ground_truth_file_path = os.path.join(
        AUDIO_DATA_ROOT_SRC_PATH, f'{Path(wav_file).stem}.txt')
    if not os.path.isfile(ground_truth_file_path):
      raise Exception(
          f'Ground truth text file does not exist! ({ground_truth_file_path})')
    wav_file_path = os.path.join(AUDIO_DATA_ROOT_SRC_PATH, wav_file)

    with open(ground_truth_file_path, 'r') as fo:
      ground_truth_text = fo.read()

    print(
        f'{Color.BLUE}{Color.BOLD}Ground truth text{Color.END}:'
        f'\n{Color.BLUE}{ground_truth_text}\n{Color.END}')
    print('-' * 20)
    for model_a in model_a_list:
      a2t_data = model_a.audio_2_text(wav_file_path)
      print(f'Transformed text ({model_a.name}):\n{a2t_data.text}\n')
      score = metric.score(a2t_data.text, ground_truth_text)
      score_table.add_row(
          [
              wav_file,
              model_a.name,
              round(score, 2),
              round(a2t_data.spent_time_sec, 2)
          ])
      model_accumulated_scores[model_a.name].append(score)
      model_accumulated_time[model_a.name].append(a2t_data.spent_time_sec)

    print('')

  print(f'{Color.BOLD}Raw data ({lang_setting}){Color.END}')
  print(score_table)
  print('')
  print(f'{Color.BOLD}Ranking Table (metric={metric.__class__}){Color.END}')
  ranking_table = PrettyTable(['Name', 'Avg. score', 'Avg. Time(s)'])
  ranking_data = []
  for model_name in model_accumulated_scores.keys():
    model_scores = model_accumulated_scores[model_name]
    model_spent_time_list = model_accumulated_time[model_name]
    avg_model_score = (
        round(sum(model_scores) / len(model_scores), 2)
        if model_scores
        else 0)
    avg_model_spent_time = (
        round(sum(model_spent_time_list) / len(model_spent_time_list), 2)
        if model_spent_time_list
        else 0)
    ranking_data.append((model_name, avg_model_score, avg_model_spent_time))

  ranking_data = sorted(
      ranking_data, key=lambda t: t[1], reverse=metric.do_sort_reverse)
  for data in ranking_data:
    ranking_table.add_row(data)
  print(ranking_table)
  print('')
