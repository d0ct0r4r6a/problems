while True:
  try:
    line = input()
  except EOFError:
    break

  cards = line.split()
  k = 0
  q = 0
  j = 0
  a = 0
  points = 0
  S = []
  H = []
  D = []
  C = []
  stopped = []
  for card in cards:
    if 'S' in card:
      S.append(card[0])
    elif 'H' in card:
      H.append(card[0])
    elif 'D' in card:
      D.append(card[0])
    elif 'C' in card:
      C.append(card[0])

    # 1
    if 'A' in card:
      a += 1
      points += 4
      stopped.append(card[1])
    elif 'K' in card:
      k += 1
      points += 3
    elif 'Q' in card:
      q += 1
      points += 2
    elif 'J' in card:
      j += 1
      points += 1

  # 2
  if 'K' in S and len(S) == 1:
    points -= 1
  if 'K' in H and len(H) == 1:
    points -= 1
  if 'K' in D and len(D) == 1:
    points -= 1
  if 'K' in C and len(C) == 1:
    points -= 1
  
  # 3
  if 'Q' in S and len(S) <= 2:
    points -= 1
  if 'Q' in H and len(H) <= 2:
    points -= 1
  if 'Q' in D and len(D) <= 2:
    points -= 1
  if 'Q' in C and len(C) <= 2:
    points -= 1
  
  # 4
  if 'J' in S and len(S) <= 3:
    points -= 1
  if 'J' in H and len(H) <= 3:
    points -= 1
  if 'J' in D and len(D) <= 3:
    points -= 1
  if 'J' in C and len(C) <= 3:
    points -= 1

  pre_five = points

  # 5
  if len(S) == 2:
    points += 1
  if len(H) == 2:
    points += 1
  if len(D) == 2:
    points += 1
  if len(C) == 2:
    points += 1

  # 6
  if len(S) == 1:
    points += 2
  if len(H) == 1:
    points += 2
  if len(D) == 1:
    points += 2
  if len(C) == 1:
    points += 2
  
  # 7
  if len(S) == 0:
    points += 2
  if len(H) == 0:
    points += 2
  if len(D) == 0:
    points += 2
  if len(C) == 0:
    points += 2

  # stopped
  if 'K' in S and len(S) >= 2:
    stopped.append('S')
  if 'K' in H and len(H) >= 2:
    stopped.append('H')
  if 'K' in D and len(D) >= 2:
    stopped.append('D')
  if 'K' in C and len(C) >= 2:
    stopped.append('C')

  if 'Q' in S and len(S) >= 3:
    stopped.append('S')
  if 'Q' in H and len(H) >= 3:
    stopped.append('H')
  if 'Q' in D and len(D) >= 3:
    stopped.append('D')
  if 'Q' in C and len(C) >= 3:
    stopped.append('C')

  if points < 14:
    print('PASS')
  else:
    if pre_five >= 16 and len(set(stopped)) == 4:
      print("BID NO-TRUMP")
    else:
      most_cards = 'S'
      most_len = len(S)
      if len(H) > most_len:
        most_cards = 'H'
        most_len = len(H)
      if len(D) > most_len:
        most_cards = 'D'
        most_len = len(D)
      if len(C) > most_len:
        most_cards = 'C'
        most_len = len(C)
      print(f"BID {most_cards}")
  
