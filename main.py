import random
import os

str = '''
 O 
/|\\
/ \\
'''

words = ['Hello Baby', 'Some Fresh Air', 'Goodby', 'Success', 'Monster', 'Give Me Space']
life = 3

print(str)

def clear_console():
  os.system('cls' if os.name == 'nt' else 'clear')

def get_random_word(list_of_words):
  value = random.randint(0, (len(list_of_words) - 1))
  selected_word = list_of_words[value]
  return selected_word

def count_letters(selected_word):
  number_of_letters = len(selected_word)
  return number_of_letters

def write_hidden_word(word):
  
  hidden_word = ''
  for letter in word:
    if letter == ' ':
      hidden_word.join(' ')
    else:
      hidden_word.join('_')
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

current_word = ''
while life != 0:
  #print(print_list_first_time(word))
  input_letter = input("Enter a letter: ")
  if input_letter not in word:
    life -= 1
  else:
    for letter in word:
      if letter == input_letter:
        current_word.join(letter)
      else:
        current_word.join('_')

  print(f'You entered: {input_letter}')
  print(f'Life remainig: {life}')
  print(f'Currente word: {current_word}', end='\n')

  try:
    pass
  except ValueError:
    print("Invalid input. Please enter a valid letter.")

#Give me space
# #___e _e ____e
#[e]