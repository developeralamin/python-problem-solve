

def my_fun():
    print("Hello, World!")
my_fun()

def add(a, b):
    return a + b
result = add(5, 3)
print("The sum is:", result)

def animal(name,age,species):
    print(f"{name} is a {age} year old {species}.")
animal("Buddy", 5, "dog")

# variable scoping 
def outer_function():
    x = "Hello"
    print(x)  
outer_function()

# //ranges 
rangess = range(1, 10)
for x in rangess:
    print(x)
print(list(rangess))

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import number

print(len(number.numbers))