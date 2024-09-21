# Function for addition
def add(num1, num2):
    return num1 + num2

# Function for subtraction
def subtract(num1, num2):
    return num1 - num2

# Function for multiplication
def multiply(num1, num2):
    return num1 * num2

# Function for division
def divide(num1, num2):
    if num2 == 0:
        return "Error: Division by zero is not allowed."
    else:
        return num1 / num2

# Function to take user input and perform calculations
def calculator():
    print("\nSimple Calculator")
    print("Select an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    choice = input("Enter choice (1/2/3/4): ")

    if choice not in ['1', '2', '3', '4']:
        print("Invalid choice. Please choose a valid operation.")
        return

    # Taking input from the user for the two numbers
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Performing the selected operation
    if choice == '1':
        result = add(num1, num2)
        print(f"The result of {num1} + {num2} is: {result}")
    elif choice == '2':
        result = subtract(num1, num2)
        print(f"The result of {num1} - {num2} is: {result}")
    elif choice == '3':
        result = multiply(num1, num2)
        print(f"The result of {num1} * {num2} is: {result}")
    elif choice == '4':
        result = divide(num1, num2)
        print(f"The result of {num1} / {num2} is: {result}")

# Running the calculator
calculator()
