import random
print("number guessing game")

number=random.randint(1,20)
#computer will select a random number between  1 and 20

chances=0
print("Guess a number between 1 and 20")
while (chances<5):
    print("User only has 5 chances")
    guess=int(input("Enter the number: "))
    if guess==number:
        print("congratulations you won")
        break
    elif guess<number:
        print("Please use higher value because your guess ia low",guess)
    else:
        print("Please use lower value because your guess is high",guess)
    chances+=1

if not chances<5:
    print("you lose")


