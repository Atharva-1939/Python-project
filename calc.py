# Function to add two numbers
def add(x, y):
    return x + y

# Function to subtract two numbers
def subtract(x, y):
    return x - y

# Function to multiply two numbers
def multiply(x, y):
    return x * y

# Function to divide two numbers
def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error! Division by zero."

# Function to display the calculator menu and get user input
def calculator():
    print("Welcome to the Simple Calculator!")
    
    # Take input for the two numbers
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    
    # Display the operation choices
    print("\nSelect an operation:")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")
    
    # Get the user's choice
    choice = input("Enter choice (1/2/3/4): ")
    
    # Perform the operation based on the user's choice
    if choice == '1':
        result = add(num1, num2)
        print(f"{num1} + {num2} = {result}")
    elif choice == '2':
        result = subtract(num1, num2)
        print(f"{num1} - {num2} = {result}")
    elif choice == '3':
        result = multiply(num1, num2)
        print(f"{num1} * {num2} = {result}")
    elif choice == '4':
        result = divide(num1, num2)
        print(f"{num1} / {num2} = {result}")
    else:
        print("Invalid input! Please choose a valid operation (1/2/3/4).")

# Main function to run the calculator
def main():
    calculator()

# Run the calculator
if __name__ == "__main__":
    main()
