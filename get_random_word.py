import random

def get_random_word(list_of_words):
  if not list_of_words:
    raise ValueError('The word list is empty, you got nothing to guess')
  return random.choice(list_of_words)
