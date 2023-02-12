"""
1. prompt for value of the radius
2. Use radius to calculate volume of a sphere
3. Use radius to calculate surface area of a sphere
"""

# Prompt the user for the radius
radius = float(input("Please enter the radius of the sphere: "))

# Calculate the volume of the sphere
volume = (4/3) * 3.14 * (radius**3)

# Calculate the surface area of the sphere
surface_area = 4 * 3.14 * (radius**2)

# Print the result
print(f"The volume of the sphere is {volume:.2f} and the surface area is {surface_area:.2f}.")


     
     
