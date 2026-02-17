import tkinter as tk
from tkinter import messagebox
import random
import string

# ---------------- Password Generator Logic ---------------- #
def generate_password():
    try:
        length = int(length_entry.get())
        if length < 4:
            messagebox.showwarning("Warning", "Password length must be at least 4")
            return
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number")
        return

    chars = ""

    if var_lower.get():
        chars += string.ascii_lowercase
    if var_upper.get():
        chars += string.ascii_uppercase
    if var_digits.get():
        chars += string.digits
    if var_symbols.get():
        chars += string.punctuation

    if chars == "":
        messagebox.showwarning("Warning", "Select at least one character type")
        return

    password = ''.join(random.choice(chars) for _ in range(length))
    result_entry.delete(0, tk.END)
    result_entry.insert(0, password)

def copy_password():
    root.clipboard_clear()
    root.clipboard_append(result_entry.get())
    messagebox.showinfo("Copied", "Password copied to clipboard")

# ---------------- GUI Window ---------------- #
root = tk.Tk()
root.title("🔐 Password Generator")
root.geometry("400x420")
root.resizable(False, False)

# ---------------- UI Elements ---------------- #
tk.Label(root, text="Automatic Password Generator", font=("Arial", 16, "bold")).pack(pady=10)

tk.Label(root, text="Password Length:", font=("Arial", 12)).pack()
length_entry = tk.Entry(root, font=("Arial", 12), justify="center")
length_entry.pack(pady=5)

# Checkboxes
var_lower = tk.BooleanVar(value=True)
var_upper = tk.BooleanVar(value=True)
var_digits = tk.BooleanVar(value=True)
var_symbols = tk.BooleanVar(value=True)

tk.Checkbutton(root, text="Include Lowercase Letters", variable=var_lower).pack(anchor="w", padx=50)
tk.Checkbutton(root, text="Include Uppercase Letters", variable=var_upper).pack(anchor="w", padx=50)
tk.Checkbutton(root, text="Include Numbers", variable=var_digits).pack(anchor="w", padx=50)
tk.Checkbutton(root, text="Include Special Characters", variable=var_symbols).pack(anchor="w", padx=50)

# Generate Button
tk.Button(root, text="Generate Password", font=("Arial", 12),
          bg="#4CAF50", fg="white", command=generate_password).pack(pady=15)

# Result Box
result_entry = tk.Entry(root, font=("Arial", 14), justify="center")
result_entry.pack(pady=10, fill="x", padx=30)

# Copy Button
tk.Button(root, text="Copy to Clipboard", font=("Arial", 11),
          bg="#2196F3", fg="white", command=copy_password).pack(pady=5)

# Run App
root.mainloop()
