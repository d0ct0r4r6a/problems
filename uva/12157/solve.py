from math import floor

T = int(input())

for t in range(T):
  pick = "Mile Juice"
  cost = 0
  N = int(input())
  durations = list(map(int, input().split()))
  mile = 0
  juice = 0
  for duration in durations:
    mile += (floor(duration / 30) +  1) * 10
    juice += (floor(duration/60) + 1) * 15
  if juice < mile:
    cost = juice
    pick = "Juice"
  elif mile < juice:
    cost = mile
    pick = "Mile"
  else:
    cost = juice

  print(f"Case {t + 1}: {pick} {cost}")