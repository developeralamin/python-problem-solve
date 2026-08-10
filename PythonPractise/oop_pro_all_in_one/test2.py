class Person:
  def __init__(self, name):
    self.name = name

  def greet(self):
    print("Hello, my name is " + self.name)

p1 = Person("Emil")
p1.greet()

# //method parameter

class Calculator:
    def add(self, x, y):
        return x + y
    
    def subtract(self, x, y):
        return x - y
calc = Calculator()
print(calc.add(5, 3))  # Output: 8
print(calc.subtract(5, 3))  # Output: 2