import sys
input = sys.stdin.readline

def get_value(card: str):
  if card[0].isnumeric():
    return int(card[0])
  else:
    return 10

T = int(input())

for t in range(T):
  Y = 0

  pile = input().split()
  hand = pile[-25:]
  pile = pile[:27]
  for _ in range(3):
    X = get_value(pile[-1])
    Y += X
    pile = pile[:len(pile) - 1 - (10 - X)]
  pile += hand
  ans = pile[Y - 1]
  print(f"Case {t + 1}: {ans}")