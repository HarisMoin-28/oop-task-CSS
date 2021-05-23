#Classes, Inheritance

#Parent Class
class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"name is {self.name} and I am {self.age} years old")

#student class
#new variable defined
class Teacher(Employee):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def info(self):
        print(f"name is {self.name} and age is {self.age} years old and I teach {self.subject}")

#instances
x = Teacher("xyz", 22, "python")
x.info()