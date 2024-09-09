# Function to add two numbers provided by the user.

def add_numbers():
    try:
        # Get input from the user and test that it is a number.
        number1 = float(input("Enter the first number: "))
        number2 = float(input("Enter the second number: "))

        # Calculate the sum of the two numbers.
        result = number1 + number2

        # Display the result.
        print(f"Number 1 = {number1}")
        print(f"Number 2 = {number2}")
        print(f"The sum is {result}")

    except ValueError:
        # Handle non numeric inputs.
        print("Invalid input. Please enter numeric values.")

add_numbers()