from utility_vars import terms_to_guess, missing_letter, max_guesses
from get_term import get_term
from write_hidden_term import write_hidden_term
from get_letter import get_letter
from check_letter_in_term import check_letter_in_term

guesses = max_guesses
term = get_term(terms_to_guess)
hidden_term = write_hidden_term(term)

print(f'This is a simple hang-man game')
print(f'The word selected is "{ term }"')
print(f'You got up to { guesses } guesses.')
print(''.join(hidden_term))
print()

while guesses:
  letter = get_letter()
  hidden_term, guesses = check_letter_in_term(letter, term, hidden_term, guesses)
  guess_word = 'guess' if guesses == 1 else 'guesses'

  if missing_letter not in hidden_term:
    print(f'😎 You guessed the term: { ''.join(hidden_term) }')
    break
  elif not guesses:
    print('💩 You are such a looser!')
    print(f'🔮 The term was: "{ term }"')
    break
  else:
    print(f'⌨️  You entered: { letter }')
    print(f'❤️  { guesses } { guess_word } remaining.')
    print(f'🕵️  Current term: {''.join(hidden_term)}')
    print()

# import os
# def clear_console():
#   os.system('cls' if os.name == 'nt' else 'clear')
# from hang_man_draw import hang_man_draw
# print(hang_man_draw)
