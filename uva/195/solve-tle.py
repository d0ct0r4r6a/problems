from collections import Counter
from sys import stdin
input = stdin.readline

cache = {}
def myFunc(c):
  return ord(c.lower()) * 2 + (-1 if not c.islower() else 0)

def get_anagram(word):
  if word in cache:
    return cache[word]
  if len(word) == 1:
    cache[word] = [word]
    return [word]
  ans = []
  for i in range(len(word)):
    for anagram in get_anagram(word[0:i] + word[i+1:]):
      anagram_word = word[i] + anagram
      if anagram_word not in ans:
        ans.append(anagram_word)
  cache[word] = ans
  return ans

T = int(input())

for _ in range(T):
  word = input().strip()
  c= Counter(word)
  if len(c.keys()) == 1:
    print(word)
    continue

  wordArr = [*word]
  wordArr.sort(key=myFunc)

  ans = get_anagram(''.join(wordArr))

  for w in ans:
    print(w)