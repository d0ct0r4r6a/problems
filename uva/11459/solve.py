import sys
input = sys.stdin.readline

T = int(input())
while T:
  T -= 1
  a, b, c = list(map(int, input().split()))
  jump = {}
  win = False
  positions = [1] * a
  current = 0
  for _ in range(b):
    begin, end = list(map(int, input().split()))
    jump[begin] = end
  for _ in range(c):
    dice = int(input())
    if win or len(positions) == 0:
      continue
    cur_pos = positions[current]
    cur_pos += dice
    if cur_pos in jump:
      cur_pos = jump[cur_pos]
    if cur_pos >= 100:
      cur_pos = 100
      win = True
    positions[current] = cur_pos
    current = (current + 1) % a
  for i, position in enumerate(positions):
    print(f"Position of player {i + 1} is {position}.")