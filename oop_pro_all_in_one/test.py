class test:
    a=10
p=test()
print(p.a)
print(test)

class Mannual:
  pass
data = Mannual()
data.name = "John"
print(data.name)

# //use __int__ method to initialize the attributes of the class
class Dynamic:
    def __init__(accesing, name, age):
        accesing.name = name
        accesing.age = age
    
    def display(accesing):
        print(f"{accesing.name} is {accesing.age} years old.")
d = Dynamic("John",36)
# print(d.name)
# print(d.age)
d.display()


class Car:
  def __init__(self, brand, model, year):
    self.brand = brand
    self.model = model
    self.year = year

  def display_info(self):
    print(f"{self.year} {self.brand} {self.model}")

car1 = Car("Toyota", "Corolla", 2020)
car1.display_info()