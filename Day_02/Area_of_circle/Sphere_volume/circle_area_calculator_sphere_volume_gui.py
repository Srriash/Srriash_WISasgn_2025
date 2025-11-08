import tkinter as tk
import math

def calculate_area():
    try:
        volume = float(entry.get())
        radius = ((3 * volume) / (4 * math.pi)) ** (1/3)
        area = math.pi * radius ** 2
        result_label.config(text=f"Area: {area:.2f}")
    except ValueError:
        result_label.config(text="Invalid input.")

root = tk.Tk()
root.title("Circle Area from Sphere Volume")

tk.Label(root, text="Sphere Volume in cm^3:").pack()
entry = tk.Entry(root)
entry.pack()

tk.Button(root, text="Calculate Area", command=calculate_area).pack()
result_label = tk.Label(root, text="Area of circle in cm^2:")
result_label.pack()

root.mainloop()
