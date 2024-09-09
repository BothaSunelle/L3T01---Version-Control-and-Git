def add_numbers():
    try:
        number1 = float(input("Enter the first number: "))
        number2 = float(input("Enter the second number: "))

        result = number1 + number2
        print(f"Number 1 = {number1}")
        print(f"Number 2 = {number2}")
        print(f"The sum is {result}")

    except ValueError:
        print("Invalid input. Please enter numeric values.")

add_numbers()