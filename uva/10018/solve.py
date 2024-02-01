import sys
input = sys.stdin.readline

N = int(input())

def is_palindrome(num):
  str_num = str(num)
  return str_num == str_num[::-1]

def get_reverse(num):
  return int(str(num)[::-1])

cache = {}

for _ in range(N):
  num = int(input())
  original = num
  if num in cache:
    count, num = cache[num]
    print(f"{count} {num}")
    continue
  num += get_reverse(num)
  count = 1
  while not is_palindrome(num):
    if num in cache:
      count, num = cache[num]
      print(f"{count} {num}")
      break
    num += get_reverse(num)
    count += 1
  cache[original] = (count, num)
  print(f"{count} {num}")
