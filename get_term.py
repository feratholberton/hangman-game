import random

def get_term(list_of_terms):
  if not list_of_terms:
    raise ValueError('The word list is empty, you got nothing to guess')
  return random.choice(list_of_terms)
