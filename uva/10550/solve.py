FULL_TURN_DEGREES = 360
TOTAL_MARKS = 40

def count_degrees(start, end, dir):
  if (start == end):
    return 0

  if (dir == 'cw'):
    if (end > start):
      marks = TOTAL_MARKS + start - end
    else:
      marks = start - end
  else: # ccw
    if (end > start):
      marks = end - start
    else:
      marks = TOTAL_MARKS + end - start
  return marks / TOTAL_MARKS * FULL_TURN_DEGREES

inputLine = list(map(int, input().split()))
while (inputLine != [0, 0, 0, 0]):
  pos, first, second, third = inputLine

  ans = 0
  # turn clockwise 2 full turns
  ans += 2 * FULL_TURN_DEGREES
  # stop at the 1st number
  ans += count_degrees(pos, first, 'cw')
  # turn counter clockwise 1 full turn
  ans += FULL_TURN_DEGREES
  # continue until 2nd number
  ans += count_degrees(first, second, 'ccw')
  # turn clockwise until 3rd number
  ans += count_degrees(second, third, 'cw')
  print(int(ans))

  inputLine = list(map(int, input().split()))
