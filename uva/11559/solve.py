while True:
  try:
    N, B, H, W = list(map(int, input().split()))
  except EOFError:
    break

  try:
    del ans
  except NameError:
    pass

  while(H):
    H -= 1
    p = int(input())
    avails = list(map(int, input().split()))
    should_skip = True
    for avail in avails:
      if (avail >= N):
        should_skip = False
        break
    if (should_skip):
      continue

    total_cost = N * p
    try:
      if (total_cost < ans):
        ans = total_cost
    except NameError:
      ans = total_cost

  try:
    if (ans > B):
      print('stay home')
    else:
      print(ans)
  except NameError:
    print('stay home')
