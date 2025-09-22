# Task 1: CLI Calculator

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error! Division by zero."
    return a / b

def calculator():
    print("===== CLI Calculator =====")
    print("Select operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exit")

    while True:
        choice = input("\nEnter choice (1/2/3/4/5): ")

        if choice == '5':
            print("Exiting... Thank you for using the calculator!")
            break

        if choice in ['1', '2', '3', '4']:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input! Please enter numbers only.")
                continue

            if choice == '1':
                print(f"Result: {add(num1, num2)}")

            elif choice == '2':
                print(f"Result: {subtract(num1, num2)}")

            elif choice == '3':
                print(f"Result: {multiply(num1, num2)}")

            elif choice == '4':
                print(f"Result: {divide(num1, num2)}")
        else:
            print("Invalid choice! Please select 1-5.")

if __name__ == "__main__":
    calculator()
