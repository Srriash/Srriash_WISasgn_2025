import math

# Ask the user for the area of the cone
print("This program calculates the area of a circle using the radius derived from the total surface area of a cone.")
cone_area = float(input("Enter the total surface area of the cone in cm^2: "))

# Ask for slant height which is required to isolate the base area
slant_height = float(input("Enter the slant height of the cone in cm: "))

# Total area = base area + lateral area = πr^2 + πr*l
# Therefore, base area = total area - lateral area
# lateral area = πr*l
# base area = πr^2
#
# Let base_area = cone_area - πr*l, solve for r numerically:

# Function to find r numerically
def find_radius(cone_area, slant_height):
    # Rearranged as a quadratic in r: πr^2 + πr*l - cone_area = 0
    # r^2 + r*l - cone_area/π = 0
    import math
    a = 1
    b = slant_height
    c = -cone_area / math.pi
    # solve quadratic: r = (-b + sqrt(b^2 - 4ac)) / 2a
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return None
    r = (-b + math.sqrt(discriminant)) / (2*a)
    return r

radius = find_radius(cone_area, slant_height)

if radius is None or radius <= 0:
    print("Invalid input. No positive real solution for radius.")
else:
    area = math.pi * radius ** 2
    print(f"The area of the circle (base of the cone) is: {area:.2f}")
