
# Conversion factors
CONVERSION_FACTORS = {
    "km_to_miles": 0.621371,
    "kg_to_pounds": 2.20462
}


# Read a number safely from the user
def read_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a number.")


# Addition
def add(a, b):
    return a + b


# Subtraction
def subtract(a, b):
    return a - b


# Multiplication
def multiply(a, b):
    return a * b


# Division
def divide(a, b):
    if b == 0:
        return "Cannot divide by zero!"
    return a / b


# Convert kilometres to miles
def km_to_miles(km):
    return km * CONVERSION_FACTORS["km_to_miles"]


# Convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


# Convert kilograms to pounds
def kg_to_pounds(kg):
    return kg * CONVERSION_FACTORS["kg_to_pounds"]


# Main calculator program
def main():
    while True:
        print("\n===== PYTHON CALCULATOR =====")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Kilometres to Miles")
        print("6. Celsius to Fahrenheit")
        print("7. Kilograms to Pounds")
        print("8. Quit")

        choice = input("Choose an option (1-8): ").strip()

        if choice == "8":
            print("Thank you for using the calculator. Goodbye!")
            break

        elif choice in ("1", "2", "3", "4"):
            a = read_number("Enter first number: ")
            b = read_number("Enter second number: ")

            if choice == "1":
                result = add(a, b)
            elif choice == "2":
                result = subtract(a, b)
            elif choice == "3":
                result = multiply(a, b)
            else:
                result = divide(a, b)

            print("Result:", result)

        elif choice == "5":
            km = read_number("Enter kilometres: ")
            print("Miles:", km_to_miles(km))

        elif choice == "6":
            celsius = read_number("Enter Celsius: ")
            print("Fahrenheit:", celsius_to_fahrenheit(celsius))

        elif choice == "7":
            kg = read_number("Enter kilograms: ")
            print("Pounds:", kg_to_pounds(kg))

        else:
            print("Invalid choice! Please select 1 to 8.")


# Run the program
if __name__ == "__main__":
    main()
