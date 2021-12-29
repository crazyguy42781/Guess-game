# a small game about guessing words
import time

secret_word = "Lolo"
guess_limit = 4
out_of_guesses = False


def guess_D():
    secret_word = "Lolo"
    guess_limit = 4
    out_of_guesses = False
    guess = ""
    guess_count = 0
    timerStart = time.time()
    while guess != secret_word and not out_of_guesses:
        if guess_count < guess_limit:
            guess = input("Enter the guessed word: ")
            guess_count += 1
            print("Wrong guess, try again!")
        else:
            out_of_guesses = True
    timeEnd = time.time()
    if out_of_guesses == True:
        print("You ran out of guesses! Game Over!")
    else:
        print("You win!!!!!, it toke you ", timeEnd - timerStart, " to guess the word correctly")
    time.sleep(0.5)
    print("Thank you for playing the game!")

guess_D()
