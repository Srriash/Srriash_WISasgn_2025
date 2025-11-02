import math

def calculate_circle_area(radius):
    return math.pi * radius ** 2

# Get input from user
try:
    radius = float(input("Enter the radius of the circle: "))
    if radius < 0:
        print("Error: Radius cannot be negative")
    else:
        area = calculate_circle_area(radius)
        print(f"The area of the circle with radius {radius} is: {area:.2f}")
except ValueError:
    print("Error: Please enter a valid number for the radius")