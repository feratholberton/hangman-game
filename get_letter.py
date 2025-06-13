def get_letter():
  letter = input("Enter a letter: ").lower()

  if not letter.isalpha() or len(letter) != 1:
    print('Please enter only 1 letter per turn')
    return ''
  else:
    return letter
