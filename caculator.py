# Python Calculator

operator = input("select an operator (+ - * /): ")
num1 = float(input("Enter the 1st number: "))
num2 = float(input("Enter the 2nd number: "))

# Will add 2 numbers
if operator == "+":
    result = num1 + num2
    print(round(result, 2))

# Will subtract 2 numbers
elif operator == "-":
    result = num1 - num2
    print(round(result, 2))

# Will multiply 2 numbers
elif operator == "*":
    result = num1 * num2
    print(round(result, 2))

# Will Divide 2 numbers
elif operator == "/":
    result = num1 / num2
    print(round(result, 2))

else:
    print(f"{operator} is an invalid operator")
