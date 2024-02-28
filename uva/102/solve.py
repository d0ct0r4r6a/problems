import sys
input = sys.stdin.readline

combinations = ['BCG', 'BGC', 'CBG', 'CGB', 'GBC', 'GCB']

while True:
  # B G C B G C B G C
  bottles = list(map(int, input().split()))
  if len(bottles) == 0:
    break
  
  min_combination = combinations[0]
  moved = sum(bottles)
  for combination in combinations:
    current_moved = 0
    for i, bottle in enumerate(bottles):
      if i < 3:
        if combination[0] == 'B':
          current_moved += 0 if i == 0 else bottle
        elif combination[0] == 'C':
          current_moved += 0 if i == 2 else bottle
        else:
          current_moved += 0 if i == 1 else bottle
      elif i < 6:
        if combination[1] == 'B':
          current_moved += 0 if i == 3 else bottle
        elif combination[1] == 'C':
          current_moved += 0 if i == 5 else bottle
        else:
          current_moved += 0 if i == 4 else bottle
      else:
        if combination[2] == 'B':
          current_moved += 0 if i == 6 else bottle
        elif combination[2] == 'C':
          current_moved += 0 if i == 8 else bottle
        else:
          current_moved += 0 if i == 7 else bottle
    if current_moved < moved:
      moved = current_moved
      min_combination = combination
  print(min_combination, moved)