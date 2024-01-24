n = int(input())
while n:
  f = int(input())
  ans = 0
  for i in range(f):
    size, count, env = list(map(int, input().split()))
    ans += size * env * (0 if count == 0 else 1)
  print(ans)
  n -= 1