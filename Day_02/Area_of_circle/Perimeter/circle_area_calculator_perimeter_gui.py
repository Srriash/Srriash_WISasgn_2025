import tkinter as tk
import math

def calculate_area():
    try:
        perimeter = float(entry.get())
        radius = perimeter / (2 * math.pi)
        area = math.pi * radius ** 2
        result_label.config(text=f"Area: {area:.2f}")
    except ValueError:
        result_label.config(text="Invalid input.")

root = tk.Tk()
root.title("Circle Area from Perimeter")

tk.Label(root, text="Perimeter of circle in cm:").pack()
entry = tk.Entry(root)
entry.pack()

tk.Button(root, text="Calculate Area", command=calculate_area).pack()
result_label = tk.Label(root, text="Area of circle in cm^2:")
result_label.pack()

root.mainloop()
