def get_car_value(prev_val, dep):
  return prev_val * (1 - dep)

loanInput = input().split()
while (int(loanInput[0]) > 0):
  max_m, dp, loan, n_records = loanInput
  owes = float(loan)
  value = float(dp) + float(loan)
  # We want to check after how many months until owes is less than the value

  max_m = int(max_m)
  monthly_payment = owes / max_m

  n_records = int(n_records)
  records = {}
  while n_records:
    month, dep = input().split()
    if (month == '0'):
      current_dep = float(dep)
    records[int(month)] = float(dep)
    n_records -= 1

  cur_m = 0
  reached = False
  value = get_car_value(value, records[0])

  while (not reached):
    if (owes < value):
      print (f"{cur_m} month{'' if cur_m == 1 else 's'}")
      reached = True
      continue
    cur_m += 1

    if (cur_m in records):
      current_dep = records[cur_m]

    owes = owes - monthly_payment
    value = get_car_value(value, current_dep)

  loanInput = input().split()
