# let's build a guess number game :
import random


def show_attempts(num):
    print(f"You have {num} attempts left")


def play():
    while True:
        guesses = 3
        program_guess = random.randint(1, 10)
        show_attempts(guesses)
        user_guess = int(input("I'm thinking of a number (1-10)! Try to guess the number: "))
        while user_guess != program_guess and guesses != 1:
            guesses -= 1
            show_attempts(guesses)
            if user_guess > program_guess:
                user_guess = int(input("Too High! Guess again: "))
            elif user_guess < program_guess:
                user_guess = int(input("Too low! Guess again: "))
        if (user_guess == program_guess):
            print("Congrats! That's it!🎉🥳")
        else:
            print(f"Yout lose!❌ The number was {program_guess}")
        choice = input("Would like to play again (yes/no) ")
        if choice.lower() == 'no':
            print('Thanks for playing!')
            break


play()
