class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."

class Student(Person):
    def __init__(self, name, age):
        super().__init__(name, age)  # Call the constructor of the parent class
        #//defult properties value
        self.student_id = 25  # Additional property for Student

obj = Student("John", 20)
print(obj.greet()) 
print(f"Student ID: {obj.student_id}")  # Output: Student ID: 25 