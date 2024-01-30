import sys
input = sys.stdin.readline
t = 0

def count_mines(grid, x,y):
  mine = 0
  top = y - 1 if y > 0 else None
  right = x + 1 if x < len(grid[0]) - 1 else None
  left = x - 1 if x > 0 else None
  bottom = y + 1 if y < len(grid) - 1 else None
  mine += 1 if top is not None and grid[top][x] == '*' else 0
  mine += 1 if top is not None and right is not None and grid[top][right] == '*' else 0
  mine += 1 if right is not None and grid[y][right] == '*' else 0
  mine += 1 if right is not None and bottom is not None and grid[bottom][right] == '*' else 0
  mine += 1 if bottom is not None and grid[bottom][x] == '*' else 0
  mine += 1 if bottom is not None and left is not None and grid[bottom][left] == '*' else 0
  mine += 1 if left is not None and grid[y][left] == '*' else 0
  mine += 1 if left is not None and top is not None and grid[top][left] == '*' else 0
  return str(mine)

while True:
  inp = input().split()

  if len(inp) == 0:
    continue
  row_count, col_count = list(map(int, inp))
  if row_count == 0 or col_count == 0:
    break
  elif t > 0:
    print('')
  t += 1
  grid = []
  filled_grid = []
  for _ in range(row_count):
    grid.append([*input().strip()])
  for i in range(row_count):
    row_grid = []
    for j in range(col_count):
      if grid[i][j] == '.':
        row_grid += [count_mines(grid,j,i)]
      else:
        row_grid += ['*']
    filled_grid.append(row_grid)

  print(f"Field #{t}:")
  for row in filled_grid:
    print(''.join(row))