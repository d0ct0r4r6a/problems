from math import ceil

while True:
  M, N = list(map(int, input().split()))
  if M == 0 and N == 0:
    break
  if M == 0 or N == 0:
    ans = 0
  elif M == 1 or N == 1:
    ans = max(M, N)
  elif M == 2:
    ans = ((N // 4 * 2) + (2 if N % 4 > 1 else (1 if N % 4 == 1 else 0))) * 2
  elif N == 2:
    ans = ((M // 4 * 2) + (2 if M % 4 > 1 else (1 if M % 4 == 1 else 0))) * 2
  else:
    ans = ceil(M * N / 2)
  print(f"{ans} knights may be placed on a {M} row {N} column board.")