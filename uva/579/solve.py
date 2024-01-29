while True:
  clock = input()
  if '0:00' == clock:
    break

  hours, minutes = clock.split(':')
  hour_degree = int(hours) / 12 * 360 % 360
  minute_degree = int(minutes) / 60 * 360 % 360
  hour_degree += int(minutes) / 60 * 30
  big_degree = max(minute_degree, hour_degree)
  small_degree = min(minute_degree, hour_degree)
  if big_degree - small_degree > 180:
    print(f"{(360 - (big_degree - small_degree)):.3f}")
  else:
    print(f"{(big_degree - small_degree):.3f}")
