T = int(input())

for t in range(T):
  N = int(input())
  high = 0
  low = 0
  walls = list(map(int, input().split()))
  for i in range(N - 1):
    if (walls[i + 1] > walls[i]):
      high += 1
    elif (walls[i + 1] < walls[i]):
      low += 1
  print(f"Case {t + 1}: {high} {low}")
