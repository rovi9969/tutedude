# Task 2: Using the Math Module for Calculations


import math


def square_root(n):
    return math.sqrt(n)


def logarithm(n):
    return math.log(n)


def sine(n):
    return math.sin(n)


def main(n):
    sqrt = square_root(n)
    log = logarithm(n)
    sin = sine(n)

    print(f"Square root: {sqrt}")
    print(f"Logarithm: {log}")
    print(f"Sine: {sin}")


number = int(input("Enter a number: "))
main(number)
