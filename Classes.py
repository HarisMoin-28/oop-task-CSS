#Create a Python class for Teacher which is inherited from Employee class.
#The constructor for the class should take three arguments - Name, Age and Subject of the teacher.
#Create a function inside the class that returns info of the teacher in this format : “name-age subject” .


#Classes, Inheritance

#Parent Class
class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        return f"name is {self.name} and age is {self.age}"

#student class
#new variable defined
class Teacher(Employee):
    def __init__(self, name, age, subject):
        self.name = name
        self.age = age
        self.subject = subject

    def show(self):
        return f"name is {self.name} and age is {self.age} and subject is {self.subject}"

#instances

y = Employee("xy", 70)
x = Teacher("xyz", 22, "python")

#printing the returned value form method defined in class
print(y.show())
print(x.show())
