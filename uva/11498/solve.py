K = int(input())
while (K):
  N, M = list(map(int, input().split()))
  while (K):
    X, Y = list(map(int, input().split()))
    if (X == N or Y == M):
      print('divisa')
    elif (X > N and Y > M):
      print('NE')
    elif (X > N and Y < M):
      print('SE')
    elif (X < N and Y < M):
      print('SO')
    elif (X < N and Y > M):
      print('NO')
    K = K - 1
  K = int(input())