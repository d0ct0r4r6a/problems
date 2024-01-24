T = int(input())

for t in range(T):
  lines = []
  for _ in range(10):
    lines.append(input().split())
  max_relevance = max([int(line[1]) for line in lines])
  print(f"Case #{t + 1}:")
  for line in lines:
    if (line[1] == str(max_relevance)):
      print(line[0])
