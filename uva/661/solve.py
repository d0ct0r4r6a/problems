case = 0
while True:
  line = input().split()
  n, m, c = list(map(int, line))
  if n == 0 and m == 0 and c == 0:
    break
  case += 1
  print(f"Sequence {case}")

  consumptions = []
  states = [False] * n
  max_c = 0
  current_c = 0

  for _ in range(n):
    consumptions.append(int(input()))

  blown = False
  for i in range(m):
    device = int(input())
    states[device - 1] = not states[device - 1]
    current_c += consumptions[device - 1] if states[device - 1] else -consumptions[device - 1]
    if current_c > c:
      blown = True
    if current_c > max_c:
      max_c = current_c
  if (blown):
    print("Fuse was blown.")
  else:
    print("Fuse was not blown.")
    print(f"Maximal power consumption was {max_c} amperes.")
  print('')