# class DOG:
#     initName = "Janapies" #attributes
#     def __init__(self,name,age): 
#      self.name = name  # Instance attribute
#      self.age = age   # Instance attribute

# #create object
# dog1 = DOG('Bublyen',34)
# print(dog1.name)
# print(dog1.initName)


class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

  def __str__(self):
     return f"{self.name}({self.age})"
p1 = Person("John", 36)
print(p1)
# del p1.age
# print(p1.age)
# del p1
# print(p1)
