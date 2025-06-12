def check_letter_in_word(letter, word, hidden_word, life):
  if letter not in word.lower():
    life -= 1
  else:
    for index, current_word_letter in enumerate(word):
      if current_word_letter.lower() == letter:
        hidden_word[index] = current_word_letter
  return hidden_word, life
