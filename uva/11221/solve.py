from math import sqrt
import sys
input = sys.stdin.readline

T = int(input())
for t in range(T):
  L = [*input()]
  clean = [char for char in L if char.isalpha()]
  print(f"Case #{t + 1}:")
  if clean != clean[::-1]:
    print("No magic :(")
    continue
  dim = sqrt(len(clean))
  if not dim.is_integer():
    print("No magic :(")
    continue
  print(round(dim))
