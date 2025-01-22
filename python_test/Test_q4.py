#4 Calculate the Cost of the painting of the Building Walls (area and Cost of both interior and exteriro wall )


area_of_Interior = int(input("Please Enter the area of Interior : "))
area_of_Exterior = int(input("Please Enter the Area of Exterior : "))
cost_of_interior  = int(input("Please Enter the Cost of Interior : "))
cost_Of_exterior   = int(input("Please Enter the Cost of Exterior : "))


final_Cost = (area_of_Interior * cost_of_interior) + (area_of_Exterior * cost_Of_exterior)

print("The final Cost is ", final_Cost)
