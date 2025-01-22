#1 Write a programme to find the area and perimeter of the following figure ( length , Breadth and radius )

# length = int(input("Enter the length of the rectangle: "))
# breadth = int(input("Enter the breadth of the rectangle: "))
# radius = int(input("Enter the radius of the semicircle: "))

# if radius * 2 != breadth:
#     print("Error: Radius is a half of the breadth of the rectangle.")
# else:
#     rectangular_area = length * breadth
#     semicircular_area = (3.14 * radius * radius) / 2
#     total_area = rectangular_area + semicircular_area

#     rectangular_perimeter = 2 * length + 2 * (breadth - radius)
#     semicircular_perimeter = 3.14 * radius
#     total_perimeter = rectangular_perimeter + semicircular_perimeter

#     print(f"The Area of diagram is {total_area} and Perimeter is {total_perimeter}")



length = int(input("Please Enter the Length of the Perimeter : "))
radius = int(input("Please Enter the radius of the Perimeter : "))

area = 2 * (length * radius ) + ((3.14 * radius * radius ) /2)
perimeter = (2 * length) + (radius * ( 2 + 3.14))

print(perimeter)
print(area)