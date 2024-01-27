from math import floor
count = 0
while True:
  try:
    n = int(input())
    if count > 0:
      print('')
    count += 1
  except EOFError:
    break
  friends = {}
  names = input().split()

  for name in names:
    friends[name] = 0
  for _ in names:
    line = input().split()
    person = line[0]
    money = int(line[1])
    friends_count = int(line[2])
    per_person_gift = floor(money / friends_count) if friends_count > 0 else 0
    for i in range(friends_count):
      friends[line[3 + i]] += per_person_gift
      friends[person] -= per_person_gift
  for name in names:
    print(f"{name} {friends[name]}")

    