from math import ceil
lyrics = "Happy birthday to you Happy birthday to you Happy birthday to Rujia Happy birthday to you"
words = lyrics.split()

n = int(input())
names = []
for _ in range(n):
  names.append(input())

for i in range(ceil(n / 16) * 16):
  current_name = names[i % n]
  print(f"{current_name}: {words[i % 16]}")
