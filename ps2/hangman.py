# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
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
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("{} words loaded.".format(len(wordlist)))
    return wordlist


def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

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
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    #pass
    for letter in secret_word:
        if letter not in letters_guessed:
            return False
    return True
#print(is_word_guessed('apple',  ['a','p','l','e','o']))

def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    #pass
    secret_word=list(secret_word)
    for i in range(0, len(secret_word)):
        if secret_word[i] not in letters_guessed:
            secret_word[i]='_ '
    return "".join(secret_word)
            
#print(get_guessed_word('apple', ['e','a','u','p']))  


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    #pass
    letters=string.ascii_lowercase
    for letter in letters_guessed:
        letters=letters.replace(letter, '')
    return letters
#print(get_available_letters(['e','i','k','p','r','a']))
    

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
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    #pass

    letter_guessed=[]
    no_warnings=3
    no_guesses=6
    vowels='aeiou'
    
    print('Welcome to the game Hangman!')
    print('I am thinking of a word that is {} letters long.'.format(len(secret_word)))
    print('You have {} warnings left.'.format(no_warnings))  
    print('--------------------')
   
    while no_guesses >0 and not is_word_guessed(secret_word,letter_guessed):
        
        print('You have {} guesses left.'.format(no_guesses))
        print('Available letters: {}'.format(get_available_letters(letter_guessed)))
        this_guess=input('Please guess a letter: ')
        
        if this_guess.isalpha():
            if this_guess in letter_guessed:
                if no_warnings !=0:
                    no_warnings -= 1
                    print("Oops! You've already guessed that letter.")
                    print("You have now {0} warnings left. \n{1}".format(no_warnings, get_guessed_word(secret_word, letter_guessed)))
                else:
                    no_guesses -= 1
            elif this_guess in secret_word:
                letter_guessed.append(this_guess)
                print("Good guess: {}".format(get_guessed_word(secret_word, letter_guessed)))
            elif this_guess in vowels:
                    no_guesses -= 2
                    letter_guessed.append(this_guess)
                    print("Oops! That letter is not in my word: {}".format(get_guessed_word(secret_word, letter_guessed)))
            else:
                no_guesses -= 1
                letter_guessed.append(this_guess)
                print("Oops! That letter is not in my word: {}".format(get_guessed_word(secret_word, letter_guessed)))
        else:
            if no_warnings !=0:
                no_warnings -= 1
                print("Oops! Not Valid. You have {0} warnings left: {1}".format(no_warnings, get_guessed_word(secret_word,letter_guessed)))
            else:
                no_guesses -= 1
                print("Oops! Not valid. You have {0} gusses left: {1}".format(no_guesses, get_guessed_word(secret_word,letter_guessed)))
        print('------------')
        
        if is_word_guessed(secret_word, letter_guessed):
            unique=[]
            for lt in secret_word:
                if lt not in unique:
                    unique.append(lt)
            return print('Congratulations, you won!\nYour total score for this game is:', no_guesses*len(unique))

        else:
            pass
    return print("Sorry, you ran out of guesses. The word was {}.".format(secret_word))
                  

# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)

# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    #pass
    my_word=my_word.replace(' ','')
    if len(my_word) != len(other_word):
        return False
    else:
        for idx in range(len(my_word)):
            if my_word[idx] != '_' and my_word[idx] != other_word[idx]:
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
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    #pass
    possible_words=[]
    for word in wordlist:
        if match_with_gaps(my_word, word):
            possible_words.append(word)
            
    if len(possible_words)==0:
        print("No matchs found")
    else:
        for possible_word in possible_words:
            print(possible_word, end=' ')
    print("")


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
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    #pass
    letter_guessed=[]
    no_warnings=3
    no_guesses=6
    vowels='aeiou'
    
    print('Welcome to the game Hangman!')
    print('I am thinking of a word that is {} letters long.'.format(len(secret_word)))
    print('You have {} warnings left.'.format(no_warnings))  
    print('--------------------')
   
    while no_guesses >0 and not is_word_guessed(secret_word,letter_guessed):
        
        print('You have {} guesses left.'.format(no_guesses))
        print('Available letters: {}'.format(get_available_letters(letter_guessed)))
        this_guess=input('Please guess a letter: ')
        
        if this_guess.isalpha():
            if this_guess in letter_guessed:
                if no_warnings !=0:
                    no_warnings -= 1
                    print("Oops! You've already guessed that letter.")
                    print("You have now {0} warnings left. \n{1}".format(no_warnings, get_guessed_word(secret_word, letter_guessed)))
                else:
                    no_guesses -= 1
            elif this_guess in secret_word:
                letter_guessed.append(this_guess)
                print("Good guess: {}".format(get_guessed_word(secret_word, letter_guessed)))
            elif this_guess in vowels:
                    no_guesses -= 2
                    letter_guessed.append(this_guess)
                    print("Oops! That letter is not in my word: {}".format(get_guessed_word(secret_word, letter_guessed)))
            else:
                no_guesses -= 1
                letter_guessed.append(this_guess)
                print("Oops! That letter is not in my word: {}".format(get_guessed_word(secret_word, letter_guessed)))
        elif this_guess=='*':
            show_possible_matches(get_guessed_word(secret_word, letter_guessed))
        else:
            if no_warnings !=0:
                no_warnings -= 1
                print("Oops! Not Valid. You have {0} warnings left: {1}".format(no_warnings, get_guessed_word(secret_word,letter_guessed)))
            else:
                no_guesses -= 1
                print("Oops! Not valid. You have {0} gusses left: {1}".format(no_guesses, get_guessed_word(secret_word,letter_guessed)))
        print('------------')
        
        if is_word_guessed(secret_word, letter_guessed):
            unique=[]
            for lt in secret_word:
                if lt not in unique:
                    unique.append(lt)
            return print('Congratulations, you won!\nYour total score for this game is:', no_guesses*len(unique))

        else:
            pass
    return print("Sorry, you ran out of guesses. The word was {}.".format(secret_word))



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    #secret_word = choose_word(wordlist)
    #secret_word='tact'
    #hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    #secret_word='apple'
    hangman_with_hints(secret_word)
