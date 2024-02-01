import sys
input = sys.stdin.readline

def get_next_dir(direction):
  if direction == (1,0):
    return (0, -1)
  elif direction == (0, -1):
    return (-1, 0)
  elif direction == (-1, 0):
    return (0, 1)
  elif direction == (0, 1):
    return (1, 0)
  
def get_right_dir(direction):
  if direction == (1,0):
    return (0, 1)
  elif direction == (0, 1):
    return (-1, 0)
  elif direction == (-1, 0):
    return (0, -1)
  elif direction == (0, -1):
    return (1, 0)

def get_next_pos(maze, current_pos, direction):
  next_pos = None
  right_dir = get_right_dir(direction)
  expect_right_pos = (current_pos[0] + right_dir[0], current_pos[1] + right_dir[1])

  while next_pos is None:
    expect_pos = (current_pos[0] + direction[0], current_pos[1] + direction[1])
    if expect_right_pos[0] < len(maze[0]) and expect_right_pos[0] >= 0 and expect_right_pos[1] < len(maze) and expect_right_pos[1] >= 0 and maze[expect_right_pos[1]][expect_right_pos[0]] == '0':
      direction = right_dir
      next_pos = expect_right_pos
    elif expect_pos[0] > len(maze[0]) - 1 or expect_pos[0] < 0 or expect_pos[1] > len(maze) - 1 or expect_pos[1] < 0 or maze[expect_pos[1]][expect_pos[0]] == '1':
      direction = get_next_dir(direction)
    else:
      next_pos = expect_pos

  return (next_pos, direction)


while True:
  b, w = list(map(int, input().split()))
  if b == 0 and w == 0:
    break
  maze = []
  visits = []
  for i in range(b):
    cells = [*input().strip()]
    maze.append(cells)
    visits.append([0] * len(cells))
  current_pos = (0, b - 1)
  direction = (1, 0)
  current_pos, direction = get_next_pos(maze, current_pos, direction)
  visits[current_pos[1]][current_pos[0]] += 1

  while current_pos != (0, b -1):
    current_pos, direction = get_next_pos(maze, current_pos, direction)
    visits[current_pos[1]][current_pos[0]] += 1

  ans = [0] * 5
  for col, visit in enumerate(visits):
    for row, cell in enumerate(visit):
      if maze[col][row] == '0':
        ans[int(cell)] += 1
  out = ''
  for a in ans:
    out += "{a:3d}".format(a=a)
  print(out)