# a small game about guessing words
import time
import random
from words import words_list


def guess_with_bot():
    word_list = random.choice(words_list)
    secret_word = word_list[random.randint(0, len(word_list) - 1)]
    guess_limit = 4
    out_of_guesses = False
    guess = ""
    guess_count = 0
    timerstart = time.time()
    while guess != secret_word and not out_of_guesses:
        if guess_count < guess_limit:
            guess = input("Enter the guessed word: ")
            guess_count += 1
            if guess != secret_word:
                print("Wrong guess, try again!")
            else:
                break
        else:
            out_of_guesses = True
    timeend = time.time()
    if out_of_guesses:
        print("You ran out of guesses! Game Over!")
    else:
        print("You win!!!!!, it toke you ", timeend - timerstart, " to guess the word correctly")
    time.sleep(0.5)
    print("Thank you for playing the game!\n")


def guess_with_friend():
    word_to_guess = input("Please enter a word for the other player to guess: ")
    guess_limit = int(input("Please enter how many gusses the other player has: "))
    guess_count = 0
    game = True
    out_of_guesses = False
    guess = ""
    timerstart = time.time()
    while game:
        guess = input("Guess the word: ")
        if guess == word_to_guess:
            timerend = time.time()
            print("You gussed it RIGHT! YOU WON!")
            print("It toke you ", timerend - timerstart, " seconds to guess the word")
            game = False
        elif guess != word_to_guess and not out_of_guesses:
            guess_count += 1
            print("Wrong guess, Try again!")
        if guess_count == guess_limit:
            print("You are out of guesses! Better luck next time!")
            game = False

    time.sleep(0.5)
    print("Thank you for playing our game!\n")
        

if __name__ == '__main__':
    game_play = True
    while game_play:
        print('Would you like to play with: ')
        print('Bot (b)')
        print('Friend (f)')
        print('Exit (e)')
        user_input = input("What is your selection? ")
        if user_input.lower() == 'b':
            guess_with_bot()
        elif user_input.lower() == 'f':
            guess_with_friend()
        elif user_input.lower() == 'e':
            game_play = False
        else:
            print("please answer with B or F\n")
