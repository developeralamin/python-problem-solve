#This is a comment
"""
First create python
"""
print("Hello, World!")
#if conditions
if 5 > 2:
   print("Five is greater than two!") 
if 5 > 2:   
     print("Five is greater than two!") 

# #variables
# number = float(344)
# number = str(34)
number = int(34.34)
print(number)

#function
x="awesome"
def myfunc():
  global x
  x = "fantastic"
myfunc()
print("Python is " + x)

import random

print(random.randrange(1, 10))

numbers = ["apple","banana","potato"]

for number in numbers:
    print(number)
# print(number[0])