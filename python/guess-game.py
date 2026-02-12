# let's build a guess number game :
import random


levels = {
    1: {"range": 10, "message": "I'm thinking of a number (1-10)!"},
    2: {"range": 50, "message": "I'm thinking of a number (1-50)!"},
    3: {"range": 100, "message": "I'm thinking of a number (1-100)!"},
}


def dificilty_level():
    print('1 -> easy')
    print('2 -> meduim')
    print('3 -> hard')
    n = int(input('Chose ur level: '))
    return n


def show_attempts(num):
    print(f"You have {num} attempts left")


def play(level):
    while True:
        remaining_attempts = 3
        secret_number = random.randint(1, levels[level]['range'])
        show_attempts(remaining_attempts)
        while True:
            try:
                user_guess = int(input(f"{levels[level]['message']} try to guess the number: "))
                break
            except ValueError:
                print('Please enter valid number!')
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
            print(f"You lose!❌ The number was {secret_number}")
        choice = input("Would like to play again (yes/no) ")
        if choice.lower() == 'no':
            print('Thanks for playing!')
            break


if __name__ == "__main__":
    level = 1
    while True:
        print('='*34)
        print('|  Welcome to guess number Game  |')
        print('|  1: start game                 |')
        print('|  2: dificilty level            |')
        print('|  3: exit                       |')
        print('='*34)
        n = int(input('Enter you choice: '))
        if n == 1:
            play(level)
        elif n == 2:
            level = dificilty_level()
        else:
            print('GoodBye!!')
            break
