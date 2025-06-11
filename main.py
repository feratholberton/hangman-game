import random
import os

words = ['Hello Baby', 'Some Fresh Air', 'Goodby', 'Success', 'Monster', 'Give Me Space']
life = 4

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_random_word(list_of_words):
    value = random.randint(0, (len(list_of_words) - 1))
    selected_word = list_of_words[value]
    print(f'The word selected is "{selected_word}"')
    return selected_word

def count_letters(selected_word):
    number_of_letters = len(selected_word)
    print(f'The selected word has {number_of_letters} letters')
    return number_of_letters

def print_word(current_word):
    for letter in current_word:
        if letter == input_letter:
            print(input_letter, end='')
        else:
            print('_', end='')

word = get_random_word(words)
count_letters(word)

while life != 0:
    for letter in word:
        if letter == ' ':
            print(' ', end='')
        else:
            print('_', end='')
    print()
    input_letter = input("Enter a letter: ")
    if input_letter not in word:
        life -= 1
    else:
        pass

    print(f'"You entered:" {input_letter}')
    print(f'"Life remainig:" {life}')
    #clear_console()

    try:
        pass
    except ValueError:
        print("Invalid input. Please enter a valid letter.")



#Give me space
#___e _e ____e

#[e]