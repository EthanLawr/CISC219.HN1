'''
This is a comment
'''
#---------------------------------
# Calc Max
#---------------------------------
def max(x,y,z):
    max = x
    if y > max:
        max = y
    if z > max:
        max = z
    return max
#---------------------------------
# Calc Min
#---------------------------------
def min(x,y,z):
    min = x
    if y < min:
        min = y
    if z < min:
        min = z
    return min
#---------------------------------
# Calc Sum
#---------------------------------
def sum(x,y,z):
    return x + y + z
#---------------------------------
# Calc Product
#---------------------------------
def prod(x,y,z):
    return x * y * z
#---------------------------------
# Get user input
#---------------------------------
a = float(input("Please enter a number: "))
b = float(input("Please enter a number: "))
c = float(input("Please enter a number: "))
print(a,b,c)
#---------------------------------
# Calc stuff
#---------------------------------

# Calculate Max
max = max(a,b,c)

# Calculate Min
min = min(a,b,c)

# Calculate Sum
sum = sum(a,b,c)

# Calculate Product
prod = prod(a,b,c)

#---------------------------------
# Display Stuff
#---------------------------------
print("The maximum is: ", max)
print("The minimum is: ", min)
print("The sum is: ", sum)
print("The product is: ", prod)
#---------------------------------