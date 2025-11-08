import math

# Ask the user for the perimeter of the circle
print("This program calculates the area of a circle using the perimeter (circumference).")
perimeter = float(input("Enter the perimeter (circumference) of the circle (in cm): "))

# Calculate the radius
radius = perimeter / (2 * math.pi)

# Calculate the area
area = math.pi * radius ** 2

print(f"The area of the circle is: {area:.2f} cm^2")
