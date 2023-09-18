import tkinter as tk

root = tk.Tk()
root.title("Entry Widget Example")

# Create Entry widgets with width and height settings
input_A = tk.Entry(root, width=30)  # Adjust width and height as needed
input_S = tk.Entry(root, width=10)  # Adjust width and height as needed
input_B = tk.Entry(root, width=30)  # Adjust width and height as needed

# Place the Entry widgets in specific rows and columns with sticky, padx, and pady settings
input_A.grid(column=1, row=3, sticky=tk.E, padx=5, pady=5)
input_S.grid(column=1, row=4, sticky=tk.NW, padx=5, pady=5)
input_B.grid(column=1, row=5, sticky=tk.E, padx=5, pady=5)

root.mainloop()
