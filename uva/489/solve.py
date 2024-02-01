import sys
input = sys.stdin.readline

while True:
  round = int(input())
  if round == -1:
    break
  solution = set([*input().strip()])
  guesses = [*input().strip()]
  correct = []
  incorrect = []
  for guess in guesses:
    if guess in incorrect or guess in correct:
      continue
    if guess in solution:
      correct.append(guess)
      solution.remove(guess)
    else:
      incorrect.append(guess)
    if len(solution) == 0:
      break
  print(f"Round {round}")
  if len(incorrect) >= 7:
    print("You lose.")
  elif len(solution) == 0:
    print("You win.")
  else:
    print("You chickened out.")
