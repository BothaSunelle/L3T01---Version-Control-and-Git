def add_numbers():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        result = num1 + num2

        print(f"Number 1 = {num1}")
        print(f"Number 2 = {num2}")
        print(f"The sum is {result}")

    except ValueError:
        print("Invalid input. Please enter numeric values.")

add_numbers()