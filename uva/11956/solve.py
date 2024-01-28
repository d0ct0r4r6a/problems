import sys

input = sys.stdin.readline

def toHex (dec):
  return f"{dec:02X}"

T = int(input())

for t in range(T):
  ans = [0] * 100
  command_string = input()
  pointer = 0
  for command in command_string:
    if command == '>':
      pointer = (pointer + 1) % 100
    elif command == '<':
      pointer = pointer - 1 if pointer - 1 >= 0 else 99
    elif command == '+':
      ans[pointer] = (ans[pointer] + 1) % 256
    elif command == '-':
      ans[pointer] = ans[pointer] - 1 if ans[pointer] - 1 >= 0 else 255
    else:
      pass
  print(f"Case {t + 1}: {' '.join(map(toHex, ans))}")