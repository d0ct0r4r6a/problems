while True:
  A, C = list(map(int, input().split()))
  if A == 0:
    break
  heights = list(map(int, input().split()))
  last = -1
  ans = 0
  for height in heights:
    if last == -1:
      ans = A - height
      last = ans
      continue

    diff = A - height
    if diff > last:
      ans += diff - last

    last = diff
  print(ans)
    