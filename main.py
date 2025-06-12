from get_random_word import get_random_word
from write_hidden_word import write_hidden_word
from hang_man_draw import hang_man_draw
from words_to_guess import words_to_guess

life = 3
word = get_random_word(words_to_guess)
hidden_word = write_hidden_word(word)

print(hang_man_draw)
print(f'The word selected is "{word}"')
print(f'Guesses left: {life}')
print(''.join(hidden_word))

while life != 0:
  input_letter = input("Enter a letter: ").lower()
  if input_letter not in word.lower():
    life -= 1
  else:
    for index, letter in enumerate(word):
      if letter.lower() == input_letter:
        hidden_word[index] = letter

  print(f'You entered: {input_letter}')
  print(f'Guesses remainig: {life}')
  print('Current word:', ''.join(hidden_word))
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