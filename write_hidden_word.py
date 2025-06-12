def write_hidden_word(word):
  hidden_word = []
  for letter in word:
    if letter == ' ':
      hidden_word.append(' ')
    else:
      hidden_word.append('_')
  return hidden_word
