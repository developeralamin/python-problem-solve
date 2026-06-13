age = 20
if age >= 80:
    print("You are an adult.")
    print("You can vote.")
elif age == 20:
    print("You are 20 years old.")

temperature = 22

if temperature > 30:
  print("It's hot outside!")
elif temperature > 26:
  print("It's warm outside")
elif temperature > 10:
  print("It's cool outside")
else:
  print("It's cold outside!")


# //one line if else statement
data = age if temperature > 15 else "Temperature is not hot"
# print(data)
print("Bigger is", data)

