import tkinter as tk
from tkinter import ttk
from scientific_name_generator import get_scientific_name

class ScientificNameGeneratorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Scientific Name Generator")
        self.root.geometry("400x250")
        
        # Create and set up the main frame
        self.main_frame = ttk.Frame(root, padding="20")
        self.main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Create title label
        title_label = ttk.Label(self.main_frame, 
                              text="Scientific Name Generator",
                              font=('Helvetica', 14, 'bold'))
        title_label.grid(row=0, column=0, columnspan=2, pady=(0, 20))
        
        # Create the input field
        ttk.Label(self.main_frame, text="Enter common name:").grid(row=1, column=0, pady=5)
        self.name_var = tk.StringVar()
        self.name_entry = ttk.Entry(self.main_frame, textvariable=self.name_var)
        self.name_entry.grid(row=1, column=1, pady=5, padx=5)
        
        # Create the convert button
        ttk.Button(self.main_frame, text="Convert", 
                  command=self.convert_name).grid(row=2, column=0, columnspan=2, pady=15)
        
        # Create result labels
        self.common_name_var = tk.StringVar()
        self.scientific_name_var = tk.StringVar()
        
        ttk.Label(self.main_frame, textvariable=self.common_name_var,
                 font=('Helvetica', 10)).grid(row=3, column=0, columnspan=2, pady=2)
        ttk.Label(self.main_frame, textvariable=self.scientific_name_var,
                 font=('Helvetica', 10, 'italic')).grid(row=4, column=0, columnspan=2, pady=2)
        
        # Bind Enter key to convert function
        self.name_entry.bind('<Return>', lambda e: self.convert_name())
        
        # Focus on entry field
        self.name_entry.focus()

    def convert_name(self):
        common_name = self.name_var.get().strip()
        if common_name:
            scientific_name = get_scientific_name(common_name)
            self.common_name_var.set(f"Common name: {common_name}")
            self.scientific_name_var.set(f"Scientific name: {scientific_name}")
            self.name_var.set("")  # Clear the input field

if __name__ == "__main__":
    root = tk.Tk()
    app = ScientificNameGeneratorGUI(root)
    root.mainloop()