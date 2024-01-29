import sys
input = sys.stdin.readline

dictionary = []
line = input().strip()
ananagram_dict = {}

while line != '#':
  dictionary += line.split()
  line = input().strip()

for i, word in enumerate(dictionary):
  sorted_word = ''.join(sorted(word.lower()))
  if sorted_word not in ananagram_dict:
    ananagram_dict[sorted_word] = i
    continue
  ananagram_dict[sorted_word] = -1

sorted_ananagrams = sorted([dictionary[index] for _, index in ananagram_dict.items() if index >= 0])
for ananagram in sorted_ananagrams:
  print(ananagram)
