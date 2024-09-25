# This is a comment
x = int(input("Please enter a number:\t"))
y = int(input("Please enter a second number:\t"))
if type(x) is str:
    print(type(x))
    print(x)
    x = int(x)
    print(type(x))
    print(x)
if type(y) is str:
    print(type(y))
    print(y)
    y = int(y)
    print(type(y))
    print(y)
print("The sum of these two numbers is", f"{x + y}.")
