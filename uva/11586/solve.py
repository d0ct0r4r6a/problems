T = int(input())
while T:
  T -= 1
  t = input()
  M = 0
  F = 0
  for c in t:
    if c == 'M':
      M += 1
    elif c == 'F':
      F += 1
  print("LOOP" if M == F and M > 1 else "NO LOOP")