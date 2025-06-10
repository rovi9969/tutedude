# Task 1: Create a Dictionary of Student Marks

result = {
    "Alice": 85,
    "Nick": 40,
    "Mike":90,
}

student = input("Enter the student's name: ")
marks = result.get(student)
if marks is None:
    print("Student not found.")
else:
    print(f"{student}'s marks: {marks}")
