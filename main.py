from get_random_word import get_random_word
from write_hidden_word import write_hidden_word

str = '''
 O 
/|\\
/ \\
'''
# print(str)

words = ['Hello Baby', 'Some Fresh Air', 'Goodby', 'Success', 'Monster', 'Give Me Space']
# words = ['Give Me Space']
# words = []
life = 3
word = get_random_word(words)
current_word = write_hidden_word(word)

print(f'The word selected is "{word}"')
print(f'Guesses left: {life}')
print(''.join(current_word))

while life != 0:
  input_letter = input("Enter a letter: ")
  if input_letter not in word:
    life -= 1
  else:
    for idx, letter in enumerate(word):
      if letter.lower() == input_letter.lower():
        current_word[idx] = letter

  print(f'You entered: {input_letter}')
  print(f'Guesses remainig: {life}')
  print('Current word:', ''.join(current_word))
  print()

  # try:
  #   pass
  # except ValueError:
  #   print("Invalid input. Please enter a valid letter.")

# import os
# def clear_console():
#   os.system('cls' if os.name == 'nt' else 'clear')
#Give me space
# #___e _e ____e
#[e]