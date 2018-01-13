import random


def getWord():
    words = [
        'apple',
        'mango',
        'banana',
        'tiger',
        'lion'
    ]

    return random.choice(words).upper()


def check(word, guesses, guess ):
    status = ''
    matches = 0
    for letter in word:
        if letter in guesses:
            status += letter
        else:
            status += '*'
        if guess == letter:
            matches +=1
    if matches > 1:
        print("Yes! The word contains",matches,guess)
    elif matches == 1:
        print("Word contains 1",guess)
    else:
        print("The word does not contain a letter",guess)
    matches = 0
    return status
