def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

def get_input():
    while True:
        try:
            x = float(input("Enter the first number: "))
            y = float(input("Enter the second number: "))
            return x, y
        except ValueError:
            print("Invalid input. Please enter numeric values.")

def perform_operation(choice, x, y):
    if choice == '1':
        return f"{x} + {y} = {add(x, y)}"
    elif choice == '2':
        return f"{x} - {y} = {subtract(x, y)}"
    elif choice == '3':
        return f"{x} * {y} = {multiply(x, y)}"
    elif choice == '4':
        return f"{x} / {y} = {divide(x, y)}"

def calculator():
    print("Welcome to the Python Calculator!")
    while True:
        print("\nSelect operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")

        choice = input("Enter choice (1/2/3/4/5): ")

        if choice in ['1', '2', '3', '4']:
            x, y = get_input()
            result = perform_operation(choice, x, y)
            print(result)

        elif choice == '5':
            print("Thank you for using the Python Calculator. Goodbye!")
            break

        else:
            print("Invalid input. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    calculator()
