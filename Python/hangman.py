import random
from words import words
import string


def validWord(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word


def hangman():
    word = validWord(words).upper()
    wordLetters = set(word)  # the letters of chosen word
    alphabet = set(string.ascii_uppercase)
    usedLetters = set()  # what user has guessed
    lives = 7

    while len(wordLetters) > 0 and lives > 0:

        # letters used
        # ''.join(['a','b' ,'c']) means string printed as 'a b c'
        print('You have guessed: ', ' '.join(usedLetters))

        # tell current word with dash
        wordList = [letter if letter in usedLetters else '-' for letter in word]
        print("lives remaining", lives, 'Current word: ', ' '.join(wordList))
        userInput = input('Guess a letter: ').upper()  # getting input
        if userInput in alphabet not in usedLetters:
            usedLetters.add(userInput)
            if userInput in wordLetters:
                wordLetters.remove(userInput)
            else:
                lives = lives-1
                print("letter not in the word")

        elif userInput in userInput:
            print('you have already guessed that letter')

        else:
            print('Invalid Guess. try again')
    if lives == 0:
        print("Sorry you lost, The correct word is ", word)
    else:
        # gets here when guessed all words
        print("congrats you have guessed the correct word ", word)


hangman()
