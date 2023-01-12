import random
print("==== Welcome to the game ====")
str = input("Please enter Rock, Paper, or Scissors: ")


r = random.randint(0, 2)
print(r)

lst = ["Rock", "Paper", "Scissors"]

if str == "Paper":
    if r == 0:
        print("You won! Opp. chose Rock")
    elif r == 1:
        print("It's a tie!")
    elif r == 2:
        print("You lost! Opp. chose Scissors")
if str == "Rock":
    if r == 0:
        print("It's a tie!")
    elif r == 1:
        print("You lost! Opp. chose Paper")
    elif r == 2:
        print("You won! Opp. chose Scissors")
if str == "Scissors":
    if r == 0:
        print("You lost! Opp. chose Rock")
    elif r == 1:
        print("You won! Opp. chose Paper")
    elif r == 2:
        print("It's a tie!")
