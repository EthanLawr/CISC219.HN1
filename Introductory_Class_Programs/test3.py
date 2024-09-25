# Initialize variables for the three numbers
x = "a"
y = "a"
z = "a"

# Loop until a valid first number is entered
while x == "a":
    try:
        x = float(input("Please enter a first number:\t"))
    except ValueError:  # Catch only ValueError exceptions
        print("You have entered an invalid value for a number. Please enter a valid number.")
        x = "a"

# Loop until a valid second number is entered
while y == "a":
    try:
        y = float(input("Please enter a second number:\t"))
    except ValueError:  # Catch only ValueError exceptions
        print("You have entered an invalid value for a number. Please enter a valid number.")
        y = "a"

# Loop until a valid third number is entered
while z == "a":
    try:
        z = float(input("Please enter a third number:\t"))
    except ValueError:  # Catch only ValueError exceptions
        print("You have entered an invalid value for a number. Please enter a valid number.")
        z = "a"

# Print the sum of the three numbers
print(f"The sum of these three numbers is {x + y + z}")

# Print the product of the three numbers
print(f"The product of these three numbers is {x * y * z}")