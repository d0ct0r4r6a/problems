while True:
  line = input()
  if line == '0':
    break
  k, m = list(map(int, line.split()))
  chosen = list(map(int, input().split()))
  fail = False
  for _ in range(m):
    ints = list(map(int, input().split()))
    all_count = ints[0]
    min_count = ints[1]
    curr_count = 0
    for i in range(all_count):
      course = ints[2 + i]
      if course in chosen:
        curr_count += 1
    if (curr_count < min_count):
      fail = True
      
  if fail:
    print("no")
  else:
    print("yes")