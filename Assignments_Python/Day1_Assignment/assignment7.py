#Program to Find the Roots of a Quadratic Equation

import math 
a = int(input("Enter value of a:")) 
b = int(input("Enter value of b:")) 
c = int(input("Enter value of c:")) 
 
d = (b**2)-4*(a*c) 
 
r1 = b + math.sqrt(d)/2*a 
r2 = b - math.sqrt(d)/2*a 
 
print(f"Square roots of the quadratic equation is {r1} and {r2}")