# file2.py
from file1 import addition, sub, mult, division, pow, sqrt

a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))

operation = input("Enter the operation (+ for addition, - for subtraction, * for multiplication, / for division, pow for power, sqrt for square root): ")

if operation == "+":
    result = addition(a, b)
elif operation == "-":
    result = sub(a, b)
elif operation == "*":
    result = mult(a, b)
elif operation == "/":
    result = division(a, b)
elif operation == "pow":
    result = pow(a, b)
elif operation == "sqrt":
    result = sqrt(a)
    print(f"The square root of {a} is: {result}")
else:
    result = "Invalid operation."

print(f"Result of {a} {operation} {b} is: {result}")
 
