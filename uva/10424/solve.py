from decimal import Decimal
cache = {}

def get_digit(num):
  if num in cache:
    return cache[num]

  if num < 10:
    cache[num] = num
    return num
  cache[num] = get_digit(sum(map(int, [*str(num)])))
  return cache[num]

def get_name_val(name):
  val = 0
  for c in name:
    if c.isalpha():
      val += ord(c) - 96
  return val

while True:
  try:
    first_name = input().lower()
    second_name = input().lower()
  except EOFError:
    break
  first_name_digit = get_digit(get_name_val(first_name))
  second_name_digit = get_digit(get_name_val(second_name))
  ratio = float(min(first_name_digit, second_name_digit) / max(first_name_digit, second_name_digit) * 100)
  print(f"{ratio:.2f} %")

