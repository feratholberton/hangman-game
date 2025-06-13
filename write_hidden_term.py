from string import whitespace
from utility_vars import missing_letter

def write_hidden_term(term):
  hidden_word = []
  for letter in term:
    if letter in whitespace:
      hidden_word.append(letter)
    else:
      hidden_word.append(missing_letter)
  return hidden_word
