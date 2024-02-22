t = 0

def is_same_side(a, b):
  return a.islower() and b.islower() or a.isupper() and b.isupper()

def check_hor (pos, rows, king):
  row = rows[pos[0]]
  # check left
  left = None
  for i in range(pos[1] - 1, -1, -1):
    if row[i] != '.':
      left = row[i]
      break
  if left is None or is_same_side(left, king):
    left = False
  elif left.lower() == 'q' or left.lower() == 'r':
    left = True
  else:
    left = False
  
  # check right
  right = None
  for i in range(pos[1] + 1, 8):
    if row[i] != '.':
      right = row[i]
      break
  if right is None or is_same_side(right, king):
    right = False
  elif right.lower() == 'q' or right.lower() == 'r':
    right = True
  else:
    right = False
  
  return left or right

def check_ver (pos, rows, king):
  col = [row[pos[1]] for row in rows]
  # check up
  top = None
  for i in range(pos[0] - 1, -1, -1):
    if col[i] != '.':
      top = col[i]
      break
  if top is None or is_same_side(top, king):
    top = False
  elif top.lower() == 'q' or top.lower() == 'r':
    top = True
  else:
    top = False
  
  # check down
  bottom = None
  for i in range(pos[0] + 1, 8):
    if col[i] != '.':
      bottom = col[i]
      break
  if bottom is None or is_same_side(bottom, king):
    bottom = False
  elif bottom.lower() == 'q' or bottom.lower() == 'r':
    bottom = True
  else:
    bottom = False
  
  return top or bottom

def check_kni (pos, rows, king):
  kni_poss = [(-1, -2), (-2, -1), (1, -2), (2, -1), (1, 2), (2, 1), (-1, 2), (-2, 1)]
  valid_kni_poss = []
  for kni_pos in kni_poss:
    if pos[0] + kni_pos[0] >= 0 and pos[0] + kni_pos[0] < 8 and pos[1] + kni_pos[1] >= 0 and pos[1] + kni_pos[1] < 8:
      valid_kni_poss.append(kni_pos)
  
  for kni_pos in valid_kni_poss:
    kni_coord = (pos[0] + kni_pos[0], pos[1] + kni_pos[1])
    piece = rows[kni_coord[0]][kni_coord[1]]
    if piece.lower() == 'n' and not is_same_side(piece, king):
      return True
  return False

def check_dia (pos, rows, king):
  is_white = king.isupper()
  piece_pos = pos
  top_left, top_right, bottom_left, bottom_right = False, False, False, False

  # check top right
  check_pawn = True
  while piece_pos[0] > 0 and piece_pos[1] < 7:
    piece_pos = (piece_pos[0] - 1, piece_pos[1] + 1)
    piece = rows[piece_pos[0]][piece_pos[1]]
    if piece == '.':
      check_pawn = False
      continue
    if is_same_side(piece, king):
      top_right = False
    else:
      if (is_white and check_pawn and piece.lower() == 'p') or piece.lower() == 'b' or piece.lower() == 'q':
        top_right = True
      else:
        top_right = False
    break

  piece_pos = pos
  # check top left
  check_pawn = True
  while piece_pos[0] > 0 and piece_pos[1] > 0:
    piece_pos = (piece_pos[0] - 1, piece_pos[1] - 1)
    piece = rows[piece_pos[0]][piece_pos[1]]
    if piece == '.':
      check_pawn = False
      continue
    if is_same_side(piece, king):
      top_left = False
    else:
      if (is_white and check_pawn and piece.lower() == 'p') or piece.lower() == 'b' or piece.lower() == 'q':
        top_left = True
      else:
        top_left = False
    break

  piece_pos = pos
  # check bottom left
  check_pawn = True
  while piece_pos[0] < 7 and piece_pos[1] > 0:
    piece_pos = (piece_pos[0] + 1, piece_pos[1] - 1)
    piece = rows[piece_pos[0]][piece_pos[1]]
    if piece == '.':
      check_pawn = False
      continue
    if is_same_side(piece, king):
      bottom_left = False
    else:
      if (not is_white and check_pawn and piece.lower() == 'p') or piece.lower() == 'b' or piece.lower() == 'q':
        bottom_left = True
      else:
        bottom_left = False
    break

  piece_pos = pos
  # check bottom right
  check_pawn = True
  while piece_pos[0] < 7 and piece_pos[1] < 7:
    piece_pos = (piece_pos[0] + 1, piece_pos[1] + 1)
    piece = rows[piece_pos[0]][piece_pos[1]]
    if piece == '.':
      check_pawn = False
      continue
    if is_same_side(piece, king):
      bottom_right = False
    else:
      if (not is_white and check_pawn and piece.lower() == 'p') or piece.lower() == 'b' or piece.lower() == 'q':
        bottom_right = True
      else:
        bottom_right = False
    break

  return top_right or top_left or bottom_left or bottom_right

def check_check(pos, rows, king):
  return check_hor(pos, rows, king)\
  or check_ver(pos, rows, king)\
  or check_kni(pos, rows, king)\
  or check_dia(pos, rows, king)


while True:
  t += 1
  rows = []
  is_all_empty = True
  for i in range(8):
    line = input()
    if line != '........':
      is_all_empty = False
    for j, char in enumerate(line):
      if char == 'k':
        bk = (i, j)
      elif char == 'K':
        wk = (i, j)
    rows.append(line)

  if is_all_empty:
    break
  input() # empty line between games

  outcome = "no"
  if check_check(wk, rows, 'K'):
    outcome = 'white'
  elif check_check(bk, rows, 'k'):
    outcome = 'black'
  print(f"Game #{t}: {outcome} king is in check.")
