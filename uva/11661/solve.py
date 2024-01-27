while True:
  L = int(input())
  if L == 0:
    break

  S = input()
  if 'Z' in S:
    print(0)
    continue

  last = None
  min = 2 * 10**6
  for i, c in enumerate(S):
    if last is None and (c == 'R' or c == 'D'):
      last = (i, c)
    if c != '.' and c != last[1]:
      dist = abs(i - last[0])
      if dist < min:
        min = dist
    if c != '.':
      last = (i, c)
  print(min)

