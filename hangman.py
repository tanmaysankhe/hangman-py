from allFunctions import getWord
from allFunctions import check

def main():
    word = getWord()
    guesses = []
    guessed = False
    fail = False
    count = 0
    print("Word length is ",len(word))

    while not guessed:
        text = 'Please enter a letter or ' + str(len(word)) + 'letter word'
        guess = input()
        guess = guess.upper()

        if guess in guesses:
            print("You already guessed ", guess)
        elif len(guess) == len(word):
            guesses.append(guess)
            if guess == word:
                guessed = True
            else:
                print("Sorry, it's incorrect")
        elif len(guess) == 1:
            guesses.append(guess)
            result = check(word,guesses,guess)
            if result== word:
                guessed = True
            else:
                print(result)
        else:
            print("Invalid entry")
        count += 1
        print(10-count,'tries remaining')
        if(count == 10):
            fail =True
            break

    if not fail:
        print("You guessed it right. The word is",word,'. You took ',len(guesses),'tries')
    else:
        print("The word is",word,". Better luck next time")
main()