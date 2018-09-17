# 2.9.1 - Coordinate geometry

# imports the square root function from the math
from math import sqrt

# variables that sets values to points
x1 = 1.0
y1 = 2.0
x2 = 1.0
y2 = 5.0

x3 = (x2 - x1) * (x2 - x1)
y3 = (y2 - y1) * (y2 - y1)

# gets the distance
point_dist = sqrt(x3 + y3)

# outputs the distance
print(f"The distance is {point_dist}.")
