from sys import stdin

inp = stdin.read()
inp.rstrip().lstrip()
lines = inp.split("\n")
T = int(lines[0])

for i, line in enumerate(lines[1:]):
  if (line == ''):
    T -= 1
    diff = -1
    if (i == 0):
      ans = 'yes'
      continue
    else:
      print(ans)
      ans = 'yes'
      if (i == len(lines) - 2):
        pass
      else:
        print('')

  if ' ' in line:
    top, bottom = list(map(int, line.split()))

    if (diff == -1):
      diff = abs(top - bottom)
    else:
      if (diff != abs(top - bottom)):
        ans = 'no'

    if (i == len(lines) - 2):
      print(ans)
