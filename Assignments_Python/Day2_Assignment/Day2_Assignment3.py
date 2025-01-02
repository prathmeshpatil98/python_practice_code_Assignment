# Convert distant given in feet and inches into meter and centimeter. 

feet = int(input("Please Enter the feet : "))
inches = int(input("Please Enter the inches : "))

meter = feet * 0.3048
centimeter = inches * 2.54

print(f"The meter is {meter}")
print(f"The centimeter is {centimeter}")

