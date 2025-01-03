# Write a program to reverse three-digit number. 

number = int(input("Enter a three-digit number: "))

# Extract the digits
hundreds = number // 100
tens = (number % 100) // 10
ones = number % 10

# Reverse the digits
reversed_number = ones * 100 + tens * 10 + hundreds

# Output the result
print("Reversed number:", reversed_number)


