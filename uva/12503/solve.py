T = int(input())
while T:
  T -= 1
  n = int(input())
  instructions = []
  pos = 0
  while n:
    n -= 1
    inst = input().lstrip()
    if (inst == 'LEFT'):
      pos -= 1
    elif (inst == 'RIGHT'):
      pos += 1
    else:
      _, _, ith = inst.lstrip().split()
      inst = instructions[int(ith) - 1]
      if (inst == 'LEFT'):
        pos -= 1
      elif (inst == 'RIGHT'):
        pos += 1
    instructions.append(inst)
  print(pos)