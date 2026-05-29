# Prompt user for inputs
try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
except ValueError:
    print("Error: Please enter valid numbers.")
    exit()

operator = input("Enter an operator (+, -, *, /): ")

# Perform operation based on the operator
if operator == "+":
    result = num1 + num2
    print(f"Result: {num1} + {num2} = {result}")
elif operator == "-":
    result = num1 - num2
    print(f"Result: {num1} - {num2} = {result}")
elif operator == "*":
    result = num1 * num2
    print(f"Result: {num1} * {num2} = {result}")
elif operator == "/":
    # Handle division by zero
    if num2 == 0:
        print("Error: Division by zero is not allowed.")
    else:
        result = num1 / num2
        print(f"Result: {num1} / {num2} = {result}")
else:
    print("Error: Invalid operator. Please use +, -, *, or /.")
    