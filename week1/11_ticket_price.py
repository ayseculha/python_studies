"""Calculate a ticket price based on age, student status and purchase time."""

age = int(input("Enter your age: "))

if age < 6:
    print("Your ticket is free")
elif 6 <= age <= 17:
    is_student = input("Are you a student? (yes/no): ")
    if is_student == "yes":
        print("Your ticket price is 80 TL")
    else:
        print("Your ticket price is 100 TL")
elif 18 <= age <= 64:
    is_student = input("Are you a student? (yes/no): ")
    purchase_time = input("When do you want to buy your ticket? (morning/night): ")
    if purchase_time == "morning" and is_student == "yes":
        print("Your ticket price is 120 TL")
    elif purchase_time == "morning" and is_student == "no":
        print("Your ticket price is 150 TL")
    elif purchase_time == "night" and is_student == "yes":
        print("Your ticket price is 150 TL")
    else:
        print("Your ticket price is 200 TL")
else:
    # Age 65 and over
    print("Your ticket price is 70 TL")