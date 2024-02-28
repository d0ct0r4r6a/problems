import sys
from collections import Counter
input = sys.stdin.readline

def is_anagram_pair(a: str, b: str):
  aCounter = Counter(a.replace(" ", ""))
  bCounter = Counter(b.replace(" ", ""))
  return aCounter == bCounter

t = int(input())
input()
for index in range(t):
  if index > 0:
    print("")

  strings = []
  while True:
    line = input().strip('\n')
    if line == '':
      break
    strings.append(line)
  strings.sort()
  for i, string in enumerate(strings):
    for j in range(i + 1, len(strings)):
      if is_anagram_pair(string, strings[j]):
        print(f"{string} = {strings[j]}")
