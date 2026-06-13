i = 0
while i < 6:
    i += 1
    if i == 2:
        continue
    print(f"Ouput is =  {i}")

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    if fruit == "banana":
        break
    print(fruit)

for x in range(10):
    if x % 2 == 0:
        print(x)

def my_fun():
    print("Hello, World!")
my_fun()