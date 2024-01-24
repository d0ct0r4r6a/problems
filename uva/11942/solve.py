N = int(input())
print("Lumberjacks:")
while N:
  N -= 1
  beards = list(map(int, input().split()))
  sorted_asc = all([beards[i + 1] >= beards[i] for i in range(9)])
  sorted_desc = all([beards[i + 1] <= beards[i] for i in range(9)])
  if (sorted_asc or sorted_desc):
    print("Ordered")
  else:
    print("Unordered")