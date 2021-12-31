# a small game about guessing words
import time



cAsk = input("Would you like to play with the bot (answer with B) or with a friend?(answer with F): ")


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

def guess_Dc():
    word_to_guess = input("Please enter a word for the other player to guess: ")
    guess_limit = int(input("Please enter how many gusses the other player has: "))
    guess_count = 0
    game = True
    out_of_guesses = False
    guess = ""
    timerStart = time.time()
    while  guess_count <= guess_limit:
        if guess == word_to_guess:
            timerEnd = time.time()
            print("You gusses it RIGHT! YOU WON!")
            print("It toke you ", timerEnd - timerStart," seconds to guess the word")
            break
        elif guess != word_to_guess and not out_of_guesses:
            print(guess)
            guess = input("Guess the word: ")
            guess_count += 1
            print("Wrong guess, Try again!")
        elif guess_count == guess_limit:
            print("You are out of guesses! Better luck next time!")
            break
                 
    time.sleep(0.5)
    print("Thank you for playing our game!")          
        
        
        


if cAsk == "B" or cAsk == "b":
    guess_D()
elif cAsk == "F" or cAsk == "f":
    guess_Dc()
else:
    print("please answer with B or F")
