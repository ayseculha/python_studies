"""Rate a password as weak, medium or strong based on its length."""

password = input("Enter your password: ")

if len(password) < 6:
    print("Password is very weak")
elif 6 <= len(password) <= 9:
    print("Password is medium")
else:
    print("Password is strong")