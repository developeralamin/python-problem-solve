import random

DiceRolling = True

while DiceRolling:
    print(random.randint(1,9))
    playAgain = input("choose to Roll Again [y/n]: ")

    if playAgain == "y":
        continue
    else:
        print("game is over")
        break
