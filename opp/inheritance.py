class College:
    def __init__(self,name):
        self.firstName = name
    def printName(self):
        print(self.firstName)

# Multiple Inheritance
class Friendly:
    def greet(self):
        print("Friendly!")

#inherite child class to parent class
class Student(College,Friendly):
    def __init__(self,name, year):
     super().__init__(name) # inherit 
     #default properties value
     self.graduationyear = 2015

    #add method
    def printGraduationYear(self):
       print(f"Graductation year {self.graduationyear}")

stdn = Student('ds',2024)
stdn.printName()
stdn.printGraduationYear()
stdn.greet()

# instituation = College(2023)
# # instituation.printName()
# instituation.printGraduationYear()
