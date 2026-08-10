a = "this is a string"
a = a.split(" ")
print(a)
a = '-'.join(a)
print(a)

#add value in index 5
data = "addfdefsld"
l = list(data)
l[5] = 'k'
data = ''.join(l)
print(data)
# print(data[5])
# data[5]='k'
# print(data)
if 5>10:
    print("5 is greater than 10")
else:    
    print("5 is less than 10")

# //boolean value
is_loggedd  = True
if is_loggedd:
    print("user is logged in")

# //casting 
a = str(10)
b = int("10")
print(a)
print(b)

# //unpacking
fruits = ["apple", "banana", "cherry"]
x,y,z= fruits
print(x,y,z)

# //set
data = set([1,2,3,4,5])
print(data)

x = set(('a', 'b', 'c'))
print(x)

import random
print(random.randint(1,10))