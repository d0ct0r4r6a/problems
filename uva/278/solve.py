from math import ceil
T = int(input())

while T:
  line = input().strip()
  if line == '':
    continue
  T -= 1
  piece, m, n = line.split()
  m = int(m)
  n = int(n)
  if piece == 'r' or piece == 'Q':
    print(min(m, n))
  elif piece == 'k':
    print(round(m * n / 2 if m * n % 2 == 0 else (m * n + 1) / 2))
  else:
    print(ceil(m / 2) * ceil(n / 2))
