sdfsdf = ("apple", "banana", "cherry")
print(sdfsdf)
print(type(sdfsdf))
print(len(sdfsdf))

tuple1 = tuple(("apple", "banana", "cherry"))
print(tuple1)

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:])

# chnage the tuple 
x = list(thistuple)
x[1] = "kiwi"
thistuple = tuple(x)
print(thistuple)

# == join tuple 
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)