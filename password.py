import random
import string

# Function to generate the password
def generate_password(length, complexity):
    if complexity == 'low':
        # Password with lowercase letters only
        characters = string.ascii_lowercase
    elif complexity == 'medium':
        # Password with lowercase and uppercase letters
        characters = string.ascii_letters
    elif complexity == 'high':
        # Password with lowercase, uppercase, digits, and punctuation
        characters = string.ascii_letters + string.digits + string.punctuation
    else:
        return "Invalid complexity level"

    # Generate the password by selecting random characters
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Main function to interact with the user
def main():
    print("Welcome to the Password Generator!")

    # User inputs for password length and complexity
    try:
        length = int(input("Enter the desired length of the password: "))
    except ValueError:
        print("Invalid input! Please enter a valid number.")
        return

    if length < 6:
        print("Password length should be at least 6 characters for better security.")
        return
    
    complexity = input("Enter the desired complexity (low, medium, high): ").lower()

    # Generate the password
    password = generate_password(length, complexity)

    # Display the generated password
    if "Invalid" in password:
        print(password)
    else:
        print(f"Your generated password is: {password}")

# Run the main function
if __name__ == "__main__":
    main()
