"""Compare two numbers and print their relationship."""

number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))

if number1 > number2:
    print("First number is greater than second number")
elif number1 == number2:
    print("Both numbers are equal")
else:
    print("First number is less than second number")