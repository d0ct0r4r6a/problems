t = int(input())
while t > 0:
  t -= 1
  s, d = list(map(int, input().split()))
  if d > s or d % 2 == 0 and s % 2 == 1 or d % 2 == 1 and s % 2 == 0:
    print('impossible')
    continue

  a = round((s + d) / 2)
  b = round(s - a)
  print(f"{a} {b}")