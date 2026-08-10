import os
f = open("demofile.txt", "r")

print(f.read())

x = open("myfile.txt",'x')
os.remove("myfile.txt")