#  Write a program to swap two numbers without using third variable

a = int(input("Please Enter the Number of a : "))
b = int(input("Please Enter the Number of B : "))

a = a + b
b = a - b
a = a - b

print(f"The value of a is {a}")

print(f"The value of b is {b}")

