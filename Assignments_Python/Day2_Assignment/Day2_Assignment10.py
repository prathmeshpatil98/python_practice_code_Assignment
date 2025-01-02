# Write a program to reverse three-digit number. 

number = int(input("Please Enter the number : "))

reverse = (number % 10) * 100 + (number % 100 // 10) * 10 + (number // 100)

print(f"The reverse of three-digit number is {reverse}")

