#Write a program to swap two numbers using third variable.

a = int(input("Please Enter the Number : "))
b = int(input("Please Enter the Number : "))

temp = a
a = b
b = temp

print(f"The value of a is {a}")
print(f"The value of b is {b}")

