import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    inFile = open(WORDLIST_FILENAME, 'r')
    line = inFile.readline()
    wordlist = line.split()
    print(len(wordlist), "words loaded.")
    return wordlist


def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
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
    for char in secret_word:
        if char not in letters_guessed:
            return False
    return True


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    guessed_word = ''
    for char in secret_word:
        if char not in letters_guessed:
            guessed_word += '_ '
        else:
            guessed_word += char
    return guessed_word


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    if letters_guessed == []:
        return string.ascii_lowercase
    else:
        available_letters = ''
        for char in string.ascii_lowercase:
            if char not in letters_guessed:
                available_letters += char
        return available_letters


def print_game_start_message(secret_word, warnings_remaining):
    '''
    secret_word: string, the word the user is guessing
    warnings_remaining: int, the number of warnings the user has remaining
    returns: None
    prints a message for the user at the start of a game
    '''
    print('Welcome to the game Hangman!')
    print('I am thinking of a word that is', len(secret_word), 'letters long.')
    print('You have', warnings_remaining, 'warnings left.')


def print_guess_start_message(guesses_remaining, letters_guessed):
    '''
    guesses_remaining: int, numbers of guesses the user has remaining
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: None
    prints a message for the user before a guess is acquired
    '''
    print('-' * 13)
    if guesses_remaining == 1:
        print('You have', guesses_remaining, 'guess left.')
    else:
        print('You have', guesses_remaining, 'guesses left.')
    print('Available letters:', get_available_letters(letters_guessed))


def print_warning_message(is_char_invalid, warnings_remaining, guessed_word):
    '''
    is_char_invalid: boolean, True if the char entered by the user is invalid, False otherwise
    warnings_remaining: int, the number of warnings the user has remaining 
    guessed_word: string, retval of get_guessed_word
    returns: None
    assumes: there are only two types of validation failures 1) invalid char or 2) letter already 
      guessed. Invalid char entries are not tracked, so multiple invalid char entries are 
      classified as invalid char validation failures rather than letter already guessed failures
    '''
    def warnings_remaining_msg(warnings_remaining):
        '''
        warnings_remaining: int, the number of warnings the user has remaining 
        returns: message for user about how many warnings they have left
        '''
        if warnings_remaining >= 0:
            if warnings_remaining == 1:
                return 'You have ' + str(warnings_remaining) + ' warning left:'
            else:
                return 'You have ' + str(warnings_remaining) + ' warnings left:'
        else:
            return 'You have no warnings left so you lose one guess:'

    def error_msg(is_char_invalid):
        '''
        is_char_invalid: boolean, True if the char entered by the user is invalid, False otherwise
        returns: message for user about the error comitted
        '''
        if is_char_invalid:
            return 'That is not a valid letter.'
        else:
            return "You've already guessed that letter."

    print(
        'Oops!', error_msg(is_char_invalid), warnings_remaining_msg(
            warnings_remaining),
        guessed_word
    )


def print_end_game_message(guesses_remaining, secret_word):
    '''
    guesses_remaining: int, the number of guesses remaining (at the end of the game)
    secret_word: string, the word the user was guessing
    returns: None
    prints a message for the user at the end of the game with their score if the user won
      and with the secret_word if they did not win
    '''
    def total_score(guesses_remaining, secret_word):
        '''
        guesses_remaining: int, the number of guesses remaining (at the end of the game)
        secret_word: string, the word the user was guessing
        returns: int, the total score associated with the winning game
        '''
        unique_secret_word = ''
        for char in secret_word:
            if char not in unique_secret_word:
                unique_secret_word += char
        return guesses_remaining * len(unique_secret_word)

    print('-' * 13)
    if guesses_remaining > 0:
        print('Congratulations, you won!')
        print('Your total score for this game is:',
              total_score(guesses_remaining, secret_word))
    else:
        print('Sorry, you ran out of guesses. The word was', secret_word + ".")


def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.
    * After each guess, you should display to the user the 
      partially guessed word so far.

    Follows the other limitations detailed in the problem write-up.
    '''
    letters_guessed = []
    guessed_word = ''
    guesses_remaining = 6
    warnings_remaining = 3
    vowels = ['a', 'e', 'i', 'o', 'u']
    print_game_start_message(secret_word, warnings_remaining)
    while guesses_remaining > 0 and not is_word_guessed(secret_word, letters_guessed):
        print_guess_start_message(guesses_remaining, letters_guessed)
        letter_guessed = str.lower(input('Please guess a letter: '))
        is_char_invalid = not str.isalpha(letter_guessed)
        is_letter_already_guessed = letter_guessed in letters_guessed
        if is_char_invalid or is_letter_already_guessed:
            if warnings_remaining <= 0:
                guesses_remaining -= 1
            warnings_remaining -= 1
            print_warning_message(
                is_char_invalid, warnings_remaining, guessed_word)
        else:
            letters_guessed.extend(letter_guessed)
            guessed_word = get_guessed_word(secret_word, letters_guessed)
            if letter_guessed in secret_word:
                print('Good guess:', guessed_word)
            else:
                if letter_guessed in vowels:
                    guesses_remaining -= 2
                else:
                    guesses_remaining -= 1
                print('Oops! That letter is not in my word:', guessed_word)
    print_end_game_message(guesses_remaining, secret_word)


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
    letters_guessed = []
    guessed_word = ''
    guesses_remaining = 6
    warnings_remaining = 3
    vowels = ['a', 'e', 'i', 'o', 'u']
    print_game_start_message(secret_word, warnings_remaining)
    while guesses_remaining > 0 and not is_word_guessed(secret_word, letters_guessed):
        print_guess_start_message(guesses_remaining, letters_guessed)
        letter_guessed = str.lower(input('Please guess a letter: '))
        is_char_invalid = not str.isalpha(letter_guessed)
        is_letter_already_guessed = letter_guessed in letters_guessed
        if letter_guessed == '*':
            print('Possible word matches are:')
            show_possible_matches(guessed_word)
        elif is_char_invalid or is_letter_already_guessed:
            if warnings_remaining <= 0:
                guesses_remaining -= 1
            warnings_remaining -= 1
            print_warning_message(
                is_char_invalid, warnings_remaining, guessed_word)
        else:
            letters_guessed.extend(letter_guessed)
            guessed_word = get_guessed_word(secret_word, letters_guessed)
            if letter_guessed in secret_word:
                print('Good guess:', guessed_word)
            else:
                if letter_guessed in vowels:
                    guesses_remaining -= 2
                else:
                    guesses_remaining -= 1
                print('Oops! That letter is not in my word:', guessed_word)
    print_end_game_message(guesses_remaining, secret_word)


if __name__ == "__main__":
    secret_word = choose_word(wordlist)
    # hangman(secret_word)
    hangman_with_hints(secret_word)
