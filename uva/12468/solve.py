a, b = list(map(int, input().split()))

while a >= 0:
  diff = abs(a - b)
  if (diff > 50):
    print(100 - diff)
  else:
    print(diff)
  a, b = list(map(int, input().split()))
