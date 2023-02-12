"""
1. prompt for value of the radius
2. Use math.pi
3. Use radius to calculate volume of a sphere
4. Use radius to calculate surface area of a sphere
"""

import math

# prompt for value of the radius
radius = float(input("Enter the radius of the sphere: "))

# Use radius to calculate volume of a sphere
volume = (4/3) * math.pi * radius**3

# Use radius to calculate surface area of a sphere
surface_area = 4 * math.pi * radius**2

# Display results
print("The volume of the sphere is {:.2f}".format(volume))
print("The surface area of the sphere is {:.2f}".format(surface_area))


