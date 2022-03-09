import random


def play():
    user = input(
        " Enter your choice! 'r' for Rock, 's' for Scissor, 'p' for Paper\n ")
    computer = random.choices(['r', 's', 'p'])
    # r>s, s>p, p>r

    if user == computer:
        return "It's a tie"
    if is_win(user, computer):
        return "You won!!!"
    return "You lost"


def is_win(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True


print(play())
