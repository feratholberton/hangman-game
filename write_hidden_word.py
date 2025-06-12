def write_hidden_word(word):
  hidden_word = []
  for character in word:
    if character == ' ':
      hidden_word.append(' ')
    else:
      hidden_word.append('_')
  return hidden_word
