import tkinter as tk
from tkinter import ttk, messagebox
import math

class CircleAreaCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Circle Area Calculator")
        self.root.geometry("300x200")
        
        # Create and set up the main frame
        self.main_frame = ttk.Frame(root, padding="20")
        self.main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Create the radius input field
        ttk.Label(self.main_frame, text="Enter radius:").grid(row=0, column=0, pady=5)
        self.radius_var = tk.StringVar()
        self.radius_entry = ttk.Entry(self.main_frame, textvariable=self.radius_var)
        self.radius_entry.grid(row=0, column=1, pady=5)
        
        # Create the calculate button
        ttk.Button(self.main_frame, text="Calculate Area", 
                  command=self.calculate_area).grid(row=1, column=0, columnspan=2, pady=10)
        
        # Create the result label
        self.result_var = tk.StringVar()
        ttk.Label(self.main_frame, textvariable=self.result_var).grid(
            row=2, column=0, columnspan=2, pady=5)
        
        # Add units label
        ttk.Label(self.main_frame, text="Units²").grid(row=0, column=2, pady=5, padx=2)

    def calculate_area(self):
        try:
            radius = float(self.radius_var.get())
            if radius < 0:
                messagebox.showerror("Error", "Radius cannot be negative!")
                return
                
            area = math.pi * radius ** 2
            self.result_var.set(f"Area: {area:.2f} units²")
            
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number!")

if __name__ == "__main__":
    root = tk.Tk()
    app = CircleAreaCalculator(root)
    root.mainloop()