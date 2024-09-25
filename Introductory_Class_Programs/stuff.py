'''
This is a comment
'''
#---------------------------------
# Get user input
#---------------------------------
a = float(input("Please enter a number: "))
b = float(input("Please enter a number: "))
c = float(input("Please enter a number: "))
print(a,b,c)
#---------------------------------
# Calc Stuff
#---------------------------------
# Calculate Max
max = a
if b > max:
    max = b
if c > max:
    max = c
# Calculate Min
min = a
if b < min:
    min = b
if c < min:
    min = c
    
# Calculate Sum
sum = a + b + c

# Calculate Product
product = a * b * c
#---------------------------------
# Display Stuff
#---------------------------------
print("The maximum is: ", max)
print("The minimum is: ", min(a,b,c))
print("The sum is: ", sum)
print("The product is: ", product)
#---------------------------------