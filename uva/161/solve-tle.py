import sys
input = sys.stdin.readline
signals = []

def get_color(signal, seconds):
  one_cycle = signal * 2
  seconds = seconds % one_cycle
  if seconds > 0 and seconds <= signal - 5:
    return 'g'
  elif seconds > signal - 5 and seconds <= signal:
    return 'o'
  else:
    return 'r'

while True: 
  line = input().strip()
  if line == '0 0 0':
    break
  signals = signals + list(map(int, line.split()))
  if 0 not in signals:
    continue
  signals = signals[:-1]
  max = 5 * 3600
  target_colors = 'g' * len(signals)

  should_return = False
  for s in range(max + 1):
    colors = ''
    for signal in signals:
      color = get_color(signal, s)
      if color == 'o' and should_return is False:
        should_return = True
      colors += color

    if should_return and colors == target_colors:
      break

  signals = []

  if colors != target_colors:
    print("Signals fail to synchronise in 5 hours")
    continue
  
  s -= 1
  seconds = s % 60
  minutes = s // 60
  hours = minutes // 60
  minutes = minutes % 60
  print(f"{hours:02d}:{minutes:02d}:{seconds:02d}")
