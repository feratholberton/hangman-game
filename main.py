from utility_vars import terms_to_guess, missing_letter, max_guesses
from get_term import get_term
from write_hidden_term import write_hidden_term
from get_letter import get_letter
from check_letter_in_term import check_letter_in_term
from massages import win_message, lose_message, in_game_message

guesses = max_guesses
term = get_term(terms_to_guess)
hidden_term = write_hidden_term(term)

print(f'You got up to { guesses } guesses.')
print(''.join(hidden_term), end='\n\n')

while guesses:
  letter = get_letter()
  hidden_term, guesses = check_letter_in_term(letter, term, hidden_term, guesses)

  if missing_letter not in hidden_term:
    win_message(term)
    break
  elif not guesses:
    lose_message(term)
    break
  else:
    in_game_message(letter, guesses, hidden_term)
