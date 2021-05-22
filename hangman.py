import string
from words import choose_word
from images import IMAGES
'''
Important instruction
* function and variable name snake_case -> is_prime
* contant variable upper case PI
'''

# tests whether the word has been correctly guessed or not


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: word guess by the user
    letters_guessed: list hold all the word guess by the user
    returns: 
      return True (if user guess the world correctly )
      return False (wrong selection)
    '''
    count = 0
    for ch in letters_guessed:
        if ch in secret_word:
            count += 1
    if len(set(secret_word)) == count:
        return True
    else:
        return False
# if you want to test this function please call function -> get_guessed_word("kindness", [k, n, d])


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: word guess by the user
    letters_guessed: list hold all the word guess by the user
    returns: 
      return string which contain all the right guessed characters
      Example :- 
      if secret_word -> "kindness" and letters_guessed = [k, n, s]
      return "k_n_n_ss"
    '''
    index = 0
    guessed_word = ""
    while (index < len(secret_word)):
        if secret_word[index] in letters_guessed:
            guessed_word += secret_word[index]
        else:
            guessed_word += "_"
        index += 1
    return guessed_word

# prints the available letters


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list contains all guessed characters
    returns: 
      it return string which contains all characters except guessed letters
    Example :-
      letters_guessed = ['e', 'a'] then    
      return sting is -> `bcdfghijklmnopqrstuvwxyz`
    '''

    letters_left = string.ascii_lowercase
    for ch in letters_guessed:
        letters_left = letters_left.replace(ch, "")
    return letters_left

# prints an image for every wrong answer


def image(chances):
    print(IMAGES[7-chances])

# checks whether input guessed is correct or not


def input_check(guess):
    if len(guess) != 1 or not guess.isalpha():
        return False
    else:
        return True

# for providing hint once


def hint(secret_word, letters_guessed):
    for ch in secret_word:
        if ch not in letters_guessed:
            print("Hint:"+ch)
            break


def hangman(secret_word):
    '''
    secret_word (string) : secret word to guessed by the user.

    Steps to start Hangman:

    * In the beginning of the game user will know about the total characters in the secret_word    

    * In each round user will guess one character 

    * After each character give feedback to the user
      * right or wrong

    * Display partial word guessed by the user and use underscore in place of not guess word    
    '''
    print("Welcome to the game, Hangman!")
    print("For hint type 'hint' and you can use it only once ")
    print("I am thinking of a word that is {} letters long.".format(
        str(len(secret_word))), end='\n\n')

    letters_guessed = []
    chances = 8
    hint_used = True
    while (chances > 0):
        available_letters = get_available_letters(letters_guessed)
        print("Available letters: {} ".format(available_letters))
        guess = input("Please guess a letter: ")
        letter = guess.lower()
        if letter == "hint" and hint_used == True:
            hint(secret_word, letters_guessed)
            hint_used = False
            continue
        if not input_check(guess):
            print("Incorrect Input ")
            continue
        if letter in secret_word:
            letters_guessed.append(letter)
            print("Good guess: {} ".format(
                get_guessed_word(secret_word, letters_guessed)))
            if is_word_guessed(secret_word, letters_guessed) == True:
                print(" * * Congratulations, you won! * * ", end='\n\n')
                break
        else:
            print("Oops! That letter is not in my word: {} ".format(
                get_guessed_word(secret_word, letters_guessed)))
            letters_guessed.append(letter)
            print("")
            chances -= 1
            print("Chances left: {} ".format(chances))
            image(chances)

        if chances == 0:
            print("You lose")


# Load the list of words into the variable wordlist
# So that it can be accessed from anywhere in the program
secret_word = choose_word()
hangman(secret_word)
