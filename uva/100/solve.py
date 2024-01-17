cache = {}

def cycle(n):
  if (n in cache):
    return cache[n]
  if (n <= 1):
    return 1

  if (n % 2 == 1):
    y = 3 * n + 1
  else:
    y = n / 2
  cache[n] = cycle(y) + 1
  return cache[n]

while True:
  try:
    i, j = list(map(int, input().split()))
  except EOFError:
    break
  ans = 0
  for n in range(min(i, j), max(i, j) + 1):
    current = cycle(n)
    if (current > ans):
      ans = current
  print(f"{i} {j} {ans}")
