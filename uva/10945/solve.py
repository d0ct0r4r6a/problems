while True:
  line = input()
  if line == 'DONE':
    break
  clean_str = ''
  reversed_str = ''
  for i in range(len(line)):
    c = line[i]
    r = line[len(line) - 1 - i]
    if c.isalpha():
      clean_str += c.lower()
    if r.isalpha():
      reversed_str += r.lower()
  if clean_str == reversed_str:
    print("You won't be eaten!")
  else:
    print("Uh oh..")