B, N = list(map(int, input().split()))

while B > 0:
  reserves = list(map(int, input().split()))
  for i in range(N):
    D, C, V = list(map(int, input().split()))
    reserves[D - 1] -= V
    reserves[C - 1] += V
  if (all(reserve >= 0 for reserve in reserves)):
    print('S')
  else:
    print('N')
  B, N = list(map(int, input().split()))
