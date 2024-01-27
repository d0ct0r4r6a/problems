while True:
  H, U, D, F = list(map(int, input().split()))
  if H == 0:
    break

  cur_h = 0
  cur_u = U
  day = 0
  F_val = F / 100 * U
  while cur_h < H and cur_h >= 0:
    # day
      day += 1
      cur_h += max(cur_u, 0)
      if (cur_h > H):
         break
    # night
      cur_h -= D
      cur_u -= F_val
      if (cur_h < 0):
         break
  outcome = "success" if cur_h > 0 else "failure"
  print(f"{outcome} on day {day}")
