thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(len(thisdict))
# //inheritance 
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age  

class Student(Person):
    pass

obj  = Student("John", 20)
print(obj.name)  # Output: John

# polymorphism  ->  
class Animal:
    def speak(self):
        return "Animal speaks"

class Dog:
    def speak(self):
        return "Woof!"
    
# inheritance polymorphsim
class Cat(Animal):
    pass

obj = Dog()
print(obj.speak())  # Output: Woof!