import json
x =  '{ "name":"John", "age":30, "city":"New York"}'

y = json.loads(x)
print(y['name'])

dictonary = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

convert = json.dumps(dictonary)
print(convert)

import re
txt = "The rain in Spain"
result = re.findall("i",txt)
if result:
    print("Matched")
else:
    print("Not matched")

print(result)

username = input("Enter username:")
print("Username is: " + username)
