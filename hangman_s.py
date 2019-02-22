import string
import random

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


wordlist = load_words()

def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''

    for ele in secret_word:
        if ele not in letters_guessed:
            return False  
    return True

def getAvailableLetters(letters_guessed):
    


    avail_letters = ''
    lettersNotGuessed = string.ascii_lowercase
    for ele in lettersNotGuessed:
        if ele not in letters_guessed:
             avail_letters += ele
    return avail_letters       
            

def get_guessed_word(secret_word, letters_guessed):

    
    index=0
    secret_word_list = list(secret_word)
    ans_list = ['_  '] * len(secret_word)
    for ele in secret_word_list:
        if ele in letters_guessed:
            ans_list[index] = ele
        index +=1
    return(''.join(ans_list))
        
def hangman(secret_word):

    name = input('\nEnter your name:-')
    print('\nHello '+name, ' Welcome to the game Hangman!! It is time to play Hangman')
    print('\nRules For the game are as follows:-\nRule 1:-You have specific number of guesses(If you choose a wrong guess one guess will be deducted).\nRule 2:-You can only enter an alphabets in lower cases.\nRule 3:-You have 3 warnings(If you enter a symbol or number or the same letter 3 times then one guess will be deducted)\nRule 4:-If you guess the letter that has not been guessed before then you losses no guess\nRule 5:-If you wrongly guessed a letter that is consonant then 1 guess will be deducted but if you guess a letter that is vowel and if it is wrong then two guess will be deducted\nRule 6:-Enter * for the hint\nRule 7:-The game will end if you have guessed the right letter or you have ran out of guesses')
    print('\nLets start the game!!')
    warnings = 3
    guesses = 6
    vowels = ['a','e','i','o','u']
    letters_guessed = []
    guess_word = []
    print('\nYou have ', warnings, 'warnings and', guesses, 'guesses')
    secret_word = choose_word(wordlist)
    lengthword = len(secret_word)
    print('\nThe length of the secretword is', lengthword)
    for char in secret_word:
        guess_word.append('_ ')
    print(guess_word)
    while (guesses > 0 and is_word_guessed(secret_word, letters_guessed) == False):
        print('\nYou have', guesses, 'Guesses Left')
        print('Available letters: ',getAvailableLetters(letters_guessed))    
        letter_guessed= str(input('Please guess a letter: '))
        is_char_invalid = not str.isalpha(letter_guessed)
        is_letter_taken = letter_guessed in letters_guessed
        if is_char_invalid:
            if warnings <= 0:
                guesses -= 1
                print('\nYou have no warnings left')
            else:
                warnings -= 1
            print('\n please Enter a valid character')
            print('\n You have ',warnings,' warnings left')
        elif is_letter_taken:
            if warnings <= 0:
                guesses -= 1
                print('\nYou have no warnings left')
            else:
                warnings -= 1
            print('\n please Enter a valid character')
            print('\n You have ',warnings,' warnings left')
        else:
            letters_guessed.extend(letter_guessed)
            guessed_word = get_guessed_word(secret_word, letters_guessed)
            if letter_guessed in secret_word:
                print('Good guess', guessed_word)
            else:
                if letter_guessed in vowels:
                    guesses -= 2
                else:
                    guesses -= 1
                print("That letter is not in secret word",guessed_word)




def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise:
    '''
    my_word = my_word.replace(' ', '')
    if len(my_word) != len(other_word):
        return False
    else:
        for i in range(len(my_word)):
            if my_word[i] != '_' and (
                my_word[i] != other_word[i]
                or my_word.count(my_word[i]) != other_word.count(my_word[i])
            ):
                return False
        return True
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass


def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.
    '''
    words_list = open(WORDLIST_FILENAME, 'r').readline().split()
    possible_matches = []
    for other_word in words_list:
        if match_with_gaps(my_word, other_word):
            possible_matches.append(other_word)
    print(' '.join(possible_matches))
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass


def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    Starts up an interactive game of Hangman.
    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses s/he starts with.
    * The user should start with 6 guesses
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.
    * After each guess, you should display to the user the
      partially guessed word so far.
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word.
    Follows the other limitations detailed in the problem write-up.
    '''
    print('\n********Welcome to the game Hangman!!**********')
    name = input('\nEnter your name:-')
    print('\nHello'+name, 'Time to play Hangman')
    print('\nRules For the game are as follows:-\nRule 1:-You have specific number of guesses(If you choose a wrong guess one guess will be deducted).\nRule 2:-You can only enter an alphabets in lower cases.\nRule 3:-You have 3 warnings(If you enter a symbol or number or the same letter 3 times then one guess will be deducted)\nRule 4:-If you guess the letter that has not been guessed before then you losses no guess\nRule 5:-If you wrongly guessed a letter that is consonant then 1 guess will be deducted but if you guess a letter that is vowel and if it is wrong then two guess will be deducted\nRule 6:-Enter * for the hint\nRule 7:-The game will end if you have guessed the right letter or you have ran out of guesses')
    print('\nLets start the game!!')
    warnings = 3
    guesses = 6
    letters_guessed = []
    vowels = ['a', 'e', 'i', 'o', 'u']
    guessed_word = ''
    guess_word = []
    print('\nYou have ', warnings, 'warnings and', guesses, 'guesses')
    secret_word = choose_word(wordlist)
    lengthword = len(secret_word)
    print('\nThe length of the secretword is', lengthword)
    for char in secret_word:
        guess_word.append('_')
    print(guess_word)
    print()
    while guesses > 0 and not is_word_guessed(secret_word, letters_guessed):
        if guesses == 1:
            print('\nYou have', guesses, 'guess left')
        else:
            print('\nYou have', guesses, 'guesses left')
        print('\nAvailable letters', getAvailableLetters(letters_guessed))
        letter_guessed = str.lower(input('Please guess a letter: '))
        is_char_invalid = not str.isalpha(letter_guessed)
        is_letter_already_taken = letter_guessed in letters_guessed
        if letter_guessed == '*':
            print('Possible word matches are:')
            show_possible_matches(guessed_word)
        elif is_char_invalid:
            if warnings <= 0:
                guesses -= 1
                print('\nYou have no warnings left so you loose one guess!!')
            else:
                warnings -= 1
                #print('\nYou have ', warnings, 'warnings left')
            print('\nPlease enter a valid character')
            print('\nYou have ', warnings, 'warnings left')
           # print('You have', guesses, 'guesses remaining')
        elif is_letter_already_taken:
            if warnings <= 0:
                guesses -= 1
                print('\nYou have no warnings left so you loose one guess!!')
            else:
                warnings -= 1
                #print('\nYou have ', warnings, 'warnings left')
            print('\nYou have already guessed that letter')
            print('\nYou have ', warnings, 'warnings left')
           # print('You have', guesses, 'guesses remaining')
        else:
            letters_guessed.extend(letter_guessed)
            guessed_word = get_guessed_word(secret_word, letters_guessed)
            if letter_guessed in secret_word:
                print('Good guess:', guessed_word)
            else:
                if letter_guessed in vowels:
                    guesses -= 2
                else:
                    guesses -= 1
                print('Oops! That letter is not in secret word:', guessed_word)
        print('\n----------------------------------------------------------')
    # print_end_game_message(guesses, secret_word)







                


    #print_end_game_message(guesses, secret_word)













if __name__ == "__main__":

    secret_word = choose_word(wordlist)

    # hangman(secret_word)

    hangman_with_hints(secret_word)








