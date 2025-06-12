from get_random_word import get_random_word
from write_hidden_word import write_hidden_word
from get_letter import get_letter
from check_letter_in_word import check_letter_in_word
from hang_man_draw import hang_man_draw
from words_to_guess import words_to_guess

print(hang_man_draw)
life = 3
word = get_random_word(words_to_guess)
hidden_word = write_hidden_word(word)

print(f'The word selected is "{word}"')
print(f'Guesses left: {life}')
print(''.join(hidden_word))
print()

while life != 0:
  letter = get_letter()
  hidden_word, life = check_letter_in_word(letter, word, hidden_word, life)

  if '_' not in hidden_word:
    print("😎 You guessed the word!")
    break
  elif life == 0:
    print("💩 You are such a looser!")
    print(f'💀 Guesses remainig: {life}')
    print(f'The word was: "{word}"')
    break
  else:
    print(f'⌨️  You entered: {letter}')
    print(f'❤️  Guesses remainig: {life}')
    print(f'🕵️  Current word: {''.join(hidden_word)}')
    print()

# import os
# def clear_console():
#   os.system('cls' if os.name == 'nt' else 'clear')
