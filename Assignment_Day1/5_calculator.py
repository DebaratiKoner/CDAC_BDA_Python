"""
### Exercise 5: Basic Operator Calculator
Create a program that takes two numbers and a math operator (`+`, `-`, `*`, `/`) from the user, performs the corresponding calculation, and prints the result.
* **Sample Input**: `num1=15`, `num2=3`, `operator='/'`
* **Sample Output**: `Result: 5.0`

"""
def calculator():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    operator = input("Enter operator (+, -, *, /): ")

    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            print("Error: Division by zero is not allowed.")
            return
    else:
        print("Error: Invalid operator.")
        return

    print(f"Result: {result}")
calculator()