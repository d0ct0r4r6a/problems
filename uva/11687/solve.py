while True:
  line = input()
  if 'END' in line:
    break
  if line == '1':
    print(1)
  elif len(line) == 1: # 9
    print(2)
  elif len(line) < 10: # 999999999
    print(3)
  elif len(line) <= 1000000:
    print(4)

