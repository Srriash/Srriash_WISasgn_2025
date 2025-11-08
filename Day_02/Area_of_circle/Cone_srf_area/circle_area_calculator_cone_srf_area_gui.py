import tkinter as tk
import math

def find_radius(cone_area, slant_height):
    a = 1
    b = slant_height
    c = -cone_area / math.pi
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return None
    r = (-b + math.sqrt(discriminant)) / (2*a)
    return r

def calculate_area():
    try:
        cone_area = float(entry_area.get())
        slant_height = float(entry_slant.get())
        radius = find_radius(cone_area, slant_height)
        if radius is None or radius <= 0:
            result_label.config(text="No valid solution for radius.")
        else:
            area = math.pi * radius ** 2
            result_label.config(text=f"Area: {area:.2f}")
    except ValueError:
        result_label.config(text="Invalid input.")

root = tk.Tk()
root.title("Circle Area from Cone Surface Area")

tk.Label(root, text="Cone Surface Area in cm^2:").pack()
entry_area = tk.Entry(root)
entry_area.pack()

tk.Label(root, text="Cone Slant Height in cm:").pack()
entry_slant = tk.Entry(root)
entry_slant.pack()

tk.Button(root, text="Calculate Area", command=calculate_area).pack()
result_label = tk.Label(root, text="Area of circle in cm^2:")
result_label.pack()

root.mainloop()
