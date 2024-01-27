def get_next_dir(dir, rotation):
  if dir == '+x':
    if rotation == '+y':
      return '+y'
    elif rotation == '-y':
      return '-y'
    elif rotation == '+z':
      return '+z'
    elif rotation == '-z':
      return '-z'
    else:
      return dir
  elif dir == '-x':
    if rotation == '+y':
      return '-y'
    elif rotation == '-y':
      return '+y'
    elif rotation == '+z':
      return '-z'
    elif rotation == '-z':
      return '+z'
    else:
      return dir
  elif dir == '+y':
    if rotation == '+y':
      return '-x'
    elif rotation == '-y':
      return '+x'
    elif rotation == '+z':
      return '+y'
    elif rotation == '-z':
      return '+y'
    else:
      return dir
  elif dir == '-y':
    if rotation == '+y':
      return '+x'
    elif rotation == '-y':
      return '-x'
    elif rotation == '+z':
      return '-y'
    elif rotation == '-z':
      return '-y'
    else:
      return dir
  elif dir == '+z':
    if rotation == '+y':
      return '+z'
    elif rotation == '-y':
      return '+z'
    elif rotation == '+z':
      return '-x'
    elif rotation == '-z':
      return '+x'
    else:
      return dir
  elif dir == '-z':
    if rotation == '+y':
      return '-z'
    elif rotation == '-y':
      return '-z'
    elif rotation == '+z':
      return '+x'
    elif rotation == '-z':
      return '-x'
    else:
      return dir

while True:
  L = int(input())
  if L == 0:
    break

  dir = '+x'
  bends = input().split()
  for bend in bends:
    prev_dir = dir
    dir = get_next_dir(dir, bend)
  print(dir)