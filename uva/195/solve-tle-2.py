from collections import Counter
from sys import stdin
from itertools import permutations
input = stdin.readline

cache = {}
def myFunc(c):
  return ord(c.lower()) * 2 + (-1 if not c.islower() else 0)

T = int(input())

for _ in range(T):
  word = input().strip()
  c= Counter(word)
  if len(c.keys()) == 1:
    print(word)
    continue

  wordArr = [*word]
  wordArr.sort(key=myFunc)

  ans = permutations(wordArr)
  printed = []
  for w in ans:
    w = ''.join(w)
    if w in printed:
      continue
    printed.append(w)
    print(w)