# let's build a guess number game :
import random


def show_attempts(num):
    print(f"You have {num} attempts left")


def play():
    while True:
        remaining_attempts = 3
        secret_number = random.randint(1, 10)
        show_attempts(remaining_attempts)
        user_guess = int(input("I'm thinking of a number (1-10)! Try to guess the number: "))
        while user_guess != secret_number and remaining_attempts > 1:
            remaining_attempts -= 1
            show_attempts(remaining_attempts)
            if user_guess > secret_number:
                user_guess = int(input("Too High! Guess again: "))
            elif user_guess < secret_number:
                user_guess = int(input("Too low! Guess again: "))
        if (user_guess == secret_number):
            print("Congrats! That's it!🎉🥳")
        else:
            print(f"Yout lose!❌ The number was {secret_number}")
        choice = input("Would like to play again (yes/no) ")
        if choice.lower() == 'no':
            print('Thanks for playing!')
            break


play()
