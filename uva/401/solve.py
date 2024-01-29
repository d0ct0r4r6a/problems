mirrored = {
  'A': 'A',
  'E': '3',
  'H': 'H',
  'I': 'I',
  'J': 'L',
  'L': 'J',
  'M': 'M',
  'O': 'O',
  'S': '2',
  'T': 'T',
  'U': 'U',
  'V': 'V',
  'W': 'W',
  'X': 'X',
  'Y': 'Y',
  'Z': '5',
  '1': '1',
  '2': 'S',
  '3': 'E',
  '5': 'Z',
  '8': '8'
}

def get_mirrored(word):
  mirrored_word = ''
  for char in word:
    if char not in mirrored:
      return '-'
    mirrored_word += mirrored[char]
  return mirrored_word[::-1]

while True:
  try:
    word = input()
  except EOFError:
    break
  mirrored_word = get_mirrored(word)
  reversed_word = word[::-1]
  is_palindrome = reversed_word == word
  
  if mirrored_word == '-' or mirrored_word != word:
    is_mirrored = False
  else:
    is_mirrored = True

  if is_mirrored and is_palindrome:
    print(f"{word} -- is a mirrored palindrome.")
  elif is_mirrored:
    print(f"{word} -- is a mirrored string.")
  elif is_palindrome:
    print(f"{word} -- is a regular palindrome.")
  else:
    print(f"{word} -- is not a palindrome.")
  print('')

  