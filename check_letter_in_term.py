def check_letter_in_term(letter, term, hidden_term, guesses):
  if letter not in term.lower():
    guesses -= 1
  else:
    for index, current_word_letter in enumerate(term):
      if current_word_letter.lower() == letter:
        hidden_term[index] = current_word_letter
  return hidden_term, guesses
