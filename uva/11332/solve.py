n = int(input())

def g(num):
  if (num < 10):
    return num
  fn = sum(map(int, [*str(num)]))
  return g(fn)

while n > 0:
  print(g(n))
  n = int(input())