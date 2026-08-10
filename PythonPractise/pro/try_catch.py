try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")


price = 59
txt = f"The price is {price} dollars"
print(txt)

x = None
print(x)

result = None
if result is None:
  print("No result yet")
else:
  print("Result is ready")



name = input("Enter your name:")
print(f"Hello {name}")
fav1 = input("What is your favorite animal:")
fav2 = input("What is your favorite color:")
fav3 = input("What is your favorite number:")
print(f"Do you want a {fav2} {fav1} with {fav3} legs?")