# Task 1: Calculate Factorial Using a Function 

def factorial(n):
    for i in range(1, n):
        n = n * i
    return n


number = int(input("Enter a number: "))
result = factorial(number)
print(f"Factorial of {number} is: {result}")
