import random

def get_random_word(list_of_words):
  if not list_of_words:
    raise ValueError('The word list is empty, you got nothing to guess')
  return random.choice(list_of_words)

# def get_random_word(list_of_words):
#   value = random.randint(0, (len(list_of_words) - 1))
#   selected_word = list_of_words[value]
#   return selected_word