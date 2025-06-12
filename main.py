import os
from get_random_word import get_random_word

str = '''
 O 
/|\\
/ \\
'''
# print(str)

words = ['Hello Baby', 'Some Fresh Air', 'Goodby', 'Success', 'Monster', 'Give Me Space']
# words = []
life = 3

def clear_console():
  os.system('cls' if os.name == 'nt' else 'clear')

def count_letters(selected_word):
  number_of_letters = len(selected_word)
  return number_of_letters

def write_hidden_word(word):
  hidden_word = ''
  for letter in word:
    if letter == ' ':
      hidden_word += ' '
    else:
      hidden_word += '_'
    return hidden_word

word = get_random_word(words)
print(f'The word selected is "{word}"')

letter_quantity = count_letters(word)
print(f'The selected word has {letter_quantity} letters')
print(f'"Life left:" {life}')

hidden_word = write_hidden_word(word)
print(hidden_word)

print()
print()
print()
print()
#current_word = print_list_first_time(word)

current_word = [' ' if c == ' ' else '_' for c in word]
while life != 0:
  #print(print_list_first_time(word))
  input_letter = input("Enter a letter: ")
  if input_letter not in word:
    life -= 1
  else:
    for idx, letter in enumerate(word):
      if letter.lower() == input_letter.lower():
        current_word[idx] = letter

  print(f'You entered: {input_letter}')
  print(f'Life remainig: {life}')
  print('Current word:', ''.join(current_word))

  try:
    pass
  except ValueError:
    print("Invalid input. Please enter a valid letter.")

#Give me space
# #___e _e ____e
#[e]