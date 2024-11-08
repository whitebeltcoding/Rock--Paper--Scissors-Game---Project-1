import random

print("===================")
print("Rock Paper Scissors")
print("===================")

print("1) ✊")
print("2) ✋")
print("3) ✌️")

player = int(input("Pick a number: "))

computer = random.randint(1,3)

if player == computer:
    print("Draw -_-")

elif player == 1 and computer == 3:
    print("Rock beats Scissors!")
    print("You chose:   ✊")
    print("Enemy chose: ✌️")
    print("You Win :)")

elif player == 1 and computer == 2:
    print("Paper covers Rock!")
    print("You chose:   ✊")
    print("Enemy chose: ✋")
    print("You Lose :(")

elif player == 2 and computer == 1:
    print("Paper covers Rock!")
    print("You chose:   ✋")
    print("Enemy chose: ✊")
    print("You Win :)")

elif player == 3 and computer == 1:
    print("Rock beats Scissors!")
    print("You chose:   ✌️")
    print("Enemy chose: ✊")
    print("You Lose :(")

elif player == 2 and computer == 3:
    print("Scissors cut Paper!")
    print("You chose:   ✋")
    print("Enemy chose: ✌️")
    print("You Lose :(")

elif player == 3 and computer == 2:
    print("Scissors cut Paper!")
    print("You chose:   ✌️")
    print("Enemy chose: ✋")
    print("You Win :)")
