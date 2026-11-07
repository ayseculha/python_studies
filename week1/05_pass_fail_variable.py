"""Same as 04_pass_fail_basic.py, but stores the result in a variable first."""

grade = int(input("Enter your grade: "))

if grade >= 60:
    result = "Passed"
else:
    result = "Failed"

print(result)