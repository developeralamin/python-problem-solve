answer = input("do you want to play this game? [Yes/No] : ").lower()

if answer == "yes":
    print("welcome to the game!")
    answer = input("Are you intersted for play a game [cave/jungle]: ").lower()
    if answer =="cave":
        print("you seen the bear in front of cave")
        answer=input("do you want to fight the bear or run [fight/run]: ").lower()
        if answer == "fight":
            print("bear is too much strong. you loos the game")
        else:
            print("you can save your life")
    elif answer == 'jungle':
        print("you see the hunter tiger. The tiger will eat you and the game will over")

else:
    print("Sorry! The Game is closed.")