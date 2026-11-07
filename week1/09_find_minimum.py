"""Find the smallest of three numbers."""

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

minimum = a
if b < minimum:
    minimum = b
if c < minimum:
    minimum = c

print("Minimum value is:", minimum)