###
## Basic online calculator
###

## Here I have defined four functions for the four
## basic operations. 
##
## 1) You should provide an interface
## function that will prompt the user for input and
## call the appropriate function based on the user's
## input. The interface function should continue to
## prompt the user for input until the user enters
## 'exit'. 
##
## 2) The interface function should also handle
## any exceptions that might be thrown by the basic
## operations functions. If an exception is thrown,
## the interface function should print an error message
## and continue to prompt the user for input.
##
## 3) Add other "operations" to the calculator, that
## involve complicated operations (e.g., trigonometric
## functions, logarithms, etc.).

import numpy as np

def add(a, b):
    """Add two numbers."""
    return a + b

def subtract(a, b):
    """Subtract one number from another."""
    return a - b

def multiply(a, b):
    """Multiply two numbers."""
    return a * b

def divide(a, b):
    """Divide one number by another."""
    return a / b

def power(a, b):
    """Raise a to the power of b."""
    return a ** b

def log(a, b):
    """Take the logarithm of a with base b."""
    return np.log(a) / np.log(b)

def sin(a):
    """Take the sine of a."""
    return np.sin(a)

def cos(a):
    """Take the cosine of a."""
    return np.cos(a)

def tan(a):
    """Take the tangent of a."""
    return np.tan(a)

def which_operation():
    operation = ""
    while operation != "exit":
        print("Which operation would you like to perform? (add, subtract, multiply, divide, exit)")
        operation = input().lower()
        if operation == "add":
            try:
                a = float(input("Enter the first number: "))
                b = float(input("Enter the second number: "))
                print(f"The sum of {a} and {b} is {add(a,b)}")
            except:
                print("Error: Please enter valid numbers.")
        elif operation == "subtract":
            try:
                a = float(input("Enter the first number: "))
                b = float(input("Enter the second number: "))
                print(f"The difference of {a} and {b} is {subtract(a,b)}")
            except:
                print("Error: Please enter valid numbers.")
        elif operation == "multiply":
            try:
                a = float(input("Enter the first number: "))
                b = float(input("Enter the second number: "))
                print(f"The product of {a} and {b} is {multiply(a,b)}")
            except:
                print("Error: Please enter valid numbers.")
        elif operation == "divide":
            try:
                a = float(input("Enter the first number: "))
                b = float(input("Enter the second number: "))
                print(f"The quotient of {a} and {b} is {divide(a,b)}")
            except:
                print("Error: Please enter valid numbers.")
        elif operation == "power":
            try:
                a = float(input("Enter the base: "))
                b = float(input("Enter the exponent: "))
                print(f"{a} raised to the power of {b} is {power(a,b)}")
            except:
                print("Error: Please enter valid numbers.")
        elif operation == "log":
            try:
                a = float(input("Enter the number: "))
                b = float(input("Enter the base: "))
                print(f"The logarithm of {a} with base {b} is {log(a,b)}")
            except:
                print("Error: Please enter valid numbers.")
        elif operation == "sin":
            try:
                a = float(input("Enter the angle in radians: "))
                print(f"The sine of {a} is {sin(a)}")
            except:
                print("Error: Please enter a valid number.")
        elif operation == "cos":
            try:
                a = float(input("Enter the angle in radians: "))
                print(f"The cosine of {a} is {cos(a)}")
            except:
                print("Error: Please enter a valid number.")
        elif operation == "tan":
            try:
                a = float(input("Enter the angle in radians: "))
                print(f"The tangent of {a} is {tan(a)}")
            except:
                print("Error: Please enter a valid number.")
        elif operation == "exit":
            return None
        else:
            print("Error: Please enter a valid operation.")
    return None