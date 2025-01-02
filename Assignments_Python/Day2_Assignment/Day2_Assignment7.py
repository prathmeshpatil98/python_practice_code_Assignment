# Find the sum of three-digit number. 

number = int(input("Please Enter the number : "))

sum = (number // 100) + (number % 100 // 10) + (number % 10)

print(f"The sum of three-digit number is {sum}")

