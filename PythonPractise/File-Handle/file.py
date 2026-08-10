f = open("demo.txt",'a')
f.write("Added new page in demo file")
f.close()

# f= open("demo.txt")
# print(f.read())

# # f = open("new.txt",'x')
# f = open("new3.txt", "w")

# f = open("new.txt",'a')
# f.write("Added text in new.txt file")
# f.close()

# f = open('new.txt')
# print(f.read())

# f = open('demo.txt')
# for x in f:
#     print(x)
# print(f.readline())

import os
if os.path.exists("new3.txt"):
  os.remove("new3.txt")
else:
  print("The file doesn't exists")