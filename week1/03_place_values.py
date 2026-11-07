"""Print the place value of each digit in a 5-digit number."""

number = int(input("Enter a 5-digit number: "))

digit1 = number // 10000
digit2 = (number // 1000) % 10
digit3 = (number // 100) % 10
digit4 = (number // 10) % 10
digit5 = number % 10

print("Ten-thousands digit:", digit1)
print("Thousands digit:", digit2)
print("Hundreds digit:", digit3)
print("Tens digit:", digit4)
print("Ones digit:", digit5)