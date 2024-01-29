from collections import Counter
card_vals = {
  '2': 2,
  '3': 3,
  '4': 4,
  '5': 5,
  '6': 6,
  '7': 7,
  '8': 8,
  '9': 9,
  'T': 10,
  'J': 11,
  'Q': 12,
  'K': 13,
  'A': 14
}

MILLION =  10 ** 6

def get_hand_val(cards):
  vals = [card_vals[card[0]] for card in cards]
  vals.sort()
  suits = [card[1] for card in cards]
  is_flush = suits[0] == suits[1] == suits[2] == suits[3] == suits[4]
  is_straight = vals[0] + 1 == vals[1] and vals[1] + 1 == vals[2] and vals[2] + 1 == vals[3] and vals[3] + 1 == vals[4]
  val_counter = Counter(vals)
  if is_flush and is_straight:
    base_val = 8 * MILLION
  elif 4 in val_counter.values():
    base_val = 7 * MILLION
    qwartet = None
    single = None
    for val, freq in val_counter.items():
      if freq == 4:
        qwartet = val
      else:
        single = val
    vals = [single] + [qwartet] * 4
  elif 3 in val_counter.values() and 2 in val_counter.values():
    base_val = 6 * MILLION
    trio = None
    duet = None
    for val, freq in val_counter.items():
      if freq == 3:
        trio = val
      else:
        duet = val
    vals = [duet] * 2 + [trio] * 3
  elif is_flush:
    base_val = 5 * MILLION
  elif is_straight:
    base_val = 4 * MILLION
  elif 3 in val_counter.values():
    base_val = 3 * MILLION
    singles = []
    trio = None
    for val, freq in val_counter.items():
      if freq == 3:
        trio = val
      else:
        singles.append(val)
    singles.sort()
    vals = singles + [trio] * 3
  elif 2 in val_counter.values():
    if len(val_counter.keys()) == 3:
      base_val = 2 * MILLION
    else:
      base_val = 1 * MILLION
    pairs = []
    singles = []
    for val, freq in val_counter.items():
      if freq == 2:
        pairs.append(val)
      else:
        singles.append(val)
    pairs.sort()
    singles.sort()
    vals = singles + pairs
  else:
    base_val = 0
  for i, val in enumerate(vals):
    base_val += val * 15 ** i
  return base_val

while True:
  try:
    line = input().split()
  except EOFError:
    break
  black_cards = line[:5]
  white_cards = line[5:]
  black_val = get_hand_val(black_cards)
  white_val = get_hand_val(white_cards)
  if black_val > white_val:
    print("Black wins.")
  elif white_val > black_val:
    print("White wins.")
  else:
    print("Tie.")
  