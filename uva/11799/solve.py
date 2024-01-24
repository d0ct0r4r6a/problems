T = int(input())
for t in range(T):
  line = list(map(int, input().split()))
  print(f"Case {t + 1}: {max(line[1:])}")