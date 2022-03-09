import random


def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Enter the guess between 1 and {x}: "))
        if guess < random_number:
            print("Sry, your guess is low, try with higher values")
        elif guess > random_number:
            print("Sry, your guess is high, try with lower values")
    print("Yay, You guessed the correct number")


guess(100)
