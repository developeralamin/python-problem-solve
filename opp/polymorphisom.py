class MainClass:
    def member(self):
        print("Main class method")

class SubClass(MainClass):
    def member(self):
        print("This is subClass") #overriding parent method

#class loop here Run-Time for Polymorphsiom 
objects = [MainClass(),SubClass()]
for obj in objects:
    obj.member()

#Compile-Time polymorphsim  overriding
class Calculator:
    def add(self, a, b=0, c=0):
        return a + b + c  # Supports multiple ways to call add()

    
cal = Calculator()
print(cal.add(3,4,4))
print(cal.add(3,4,6))