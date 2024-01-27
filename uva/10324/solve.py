count = 0
while True:
  try:
    bits = input()
    if (bits == '' or "\n" in bits):
      break
    change_counts = []
    for index in range(len(bits)):
      if index == 0:
        change_counts.append(0)
      else:
        change_counts.append(change_counts[index - 1] + 1 if bits[index] != bits[index - 1] else change_counts[index - 1])
    count += 1
    print(f"Case {count}:")
  except EOFError:
    break
  n = int(input())
  for _ in range(n):
    i, j = list(map(int, input().split()))
    print("Yes" if change_counts[i] == change_counts[j] else "No")