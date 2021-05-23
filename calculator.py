#Obevtive: To create program of a simple calculator
#which would take two inputs from the user
#and perform opreations such as addition, subtraction, multiplication, division.

#Defining functions
def add(a,b):
    """this function adds two number"""
    return a + b

def subtract(a,b):
    """this function subtracts two number"""
    return a - b

def multiply(a,b):
    """this function multiplies two number"""
    return a * b

def divide(a,b):
    """this function divides two number"""
    return a/b

#input from the user
print("Select operation: ")
print("1.Addition")
print("2.Subtraction")
print("3.multiplication")
print("4.Division")
choice = input("Enter choice(1/2/3/4):")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

#Calculation

if choice == "1":
    print(num1, "+", num2, "=", add(num1,num2))

elif choice == "2":
    print(num1, "-", num2, "=", subtract(num1,num2))

elif choice == "3":
    print(num1, "*", num2, "=", multiply(num1,num2))

elif choice == "4":
    print(num1, "/", num2, "=", divide(num1,num2))

else:
    print("Invalid input.")


