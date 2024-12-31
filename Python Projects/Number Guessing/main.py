#Range the Random Number
import  random

RandomNumber = random.randrange(1,200)
# print(RandomNumber)
inputNumber = int(input("prompt the guess number: "))

if inputNumber > RandomNumber :
    print("The number is high")
elif inputNumber < RandomNumber :
    print("The number is low")
else:
    print("❤️ Your number is matched")