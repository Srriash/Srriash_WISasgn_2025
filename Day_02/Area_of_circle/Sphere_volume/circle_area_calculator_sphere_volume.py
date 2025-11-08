import math

# Ask the user for the volume of the sphere
print("This program calculates the area of a circle using the radius derived from the volume of a sphere.")
volume = float(input("Enter the volume of the sphere in cm^3: "))

# Calculate the radius of the sphere
radius = ( (3 * volume) / (4 * math.pi) ) ** (1/3)

# Calculate the area of the circle (with same radius)
area = math.pi * radius ** 2

print(f"The area of the circle (using the radius of the sphere) is: {area:.2f}")
