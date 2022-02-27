import random


def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Enter the guess between 1 and {x}: "))
        if guess < random_number:
            print("Your guess is low")
        elif guess > random_number:
            print("Your guess is high")
        else:
            print("You've got the correct number, Amazing !!!")


guess(10)


def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(
            f"Is {guess} is too High (H), too low (L), Correct (C)???  ").lower()
        if feedback == 'h':
            high = guess-1
        elif feedback == 'l':
            low = guess+1
    print(f"Yay, your guessing number is {guess}")


computer_guess(1000)
