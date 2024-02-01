from math import ceil
import sys

input = sys.stdin.readline
signals = []

def get_cycle_string(signal):
  st = ''
  one_cycle = signal * 2
  for seconds in range(1, one_cycle + 1):
    seconds = seconds % one_cycle
    if seconds > 0 and seconds <= signal - 5:
      st += '1'
    else:
      st += '0'
  rep = ceil(5 * 3600 / one_cycle)
  st = st * rep
  extra_second = 18001
  extra_second = extra_second % one_cycle
  if extra_second > 0 and extra_second <= signal - 5:
    st += '1'
  else:
    st += '0'
  return st[:18001]

all_lines = ''
while True:
  line = input().strip()
  if line == '0 0 0':
    break
  all_lines += ' ' + line

raw_scenarios = all_lines.strip().split(' 0')
scenarios = []
for raw_scenario in raw_scenarios:
  raw_scenario = raw_scenario.strip()
  if len(raw_scenario) == 0:
    continue

  scenarios.append(list(map(int, raw_scenario.split())))

for scenario in scenarios:
  sequence_ints = []
  for signal in scenario:
    sequence_ints.append(get_cycle_string(signal))

  for i, sequence in enumerate(sequence_ints):
    if (i == 0):
      res = int(sequence, base=2)
    else:
      res = res & int(sequence, base=2)

  binary = bin(res)[2:]
  binary = binary.lstrip('1')

  if '1' not in binary:
    print("Signals fail to synchronise in 5 hours")
    continue
  else:
    ans = binary.index('1') + min(scenario) - 5
  print(f"{ans // 3600:02d}:{ans // 60 % 60:02d}:{ans % 60:02d}")
