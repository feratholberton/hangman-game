def win_message(term):
  print(f'😎 You guessed the term: { ''.join(term) }')

def lose_message(term):
  print('💩 You are such a looser!')
  print(f'🔮 The term was: "{ term }"')

def in_game_message(letter, guesses, hidden_term):
  guess_word = 'guess' if guesses == 1 else 'guesses'
  print(f'⌨️  You entered: { letter }')
  print(f'❤️  { guesses } { guess_word } remaining.')
  print(f'🕵️  Current term: { ''.join(hidden_term) }', end='\n\n')
  