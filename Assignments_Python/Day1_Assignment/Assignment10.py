# write a program to calculate area of equilateral triangle

import math

side = int(input("Enter the side of equilateral triangle : "))

sqr = math.sqrt (3)

area =sqr / 4 * side *side
print(area,"is area of equilateral triangle")