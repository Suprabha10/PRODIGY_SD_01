import tkinter as tk
from tkinter import messagebox

# Functions to perform the temperature conversions
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

# Function to handle the conversion based on user input
def convert_temperature():
    temp_input = entry.get()
    
    if not temp_input:  # Check if the entry is empty
        messagebox.showerror("Input Error", "Please enter a temperature value.")
        return
    
    try:
        temp = float(temp_input)
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid number for the temperature.")
        return
    
    unit = unit_var.get()

    if unit == 'C':
        f = celsius_to_fahrenheit(temp)
        k = celsius_to_kelvin(temp)
    elif unit == 'F':
        f = temp
        temp = fahrenheit_to_celsius(temp)
        k = fahrenheit_to_kelvin(f)
    elif unit == 'K':
        k = temp
        temp = kelvin_to_celsius(temp)
        f = kelvin_to_fahrenheit(k)

    messagebox.showinfo("Conversion Result", f"{temp:.2f} {unit} is {f:.2f} Fahrenheit and {k:.2f} Kelvin")

# Creating the main window
root = tk.Tk()
root.title("Temperature Converter")

# Creating widgets
tk.Label(root, text="Enter Temperature:").grid(row=0, column=0, padx=10, pady=10)
entry = tk.Entry(root)
entry.grid(row=0, column=1, padx=10, pady=10)

unit_var = tk.StringVar(value='C')
tk.Radiobutton(root, text="Celsius", variable=unit_var, value='C').grid(row=1, column=0)
tk.Radiobutton(root, text="Fahrenheit", variable=unit_var, value='F').grid(row=1, column=1)
tk.Radiobutton(root, text="Kelvin", variable=unit_var, value='K').grid(row=1, column=2)

tk.Button(root, text="Convert", command=convert_temperature).grid(row=2, columnspan=3, pady=10)

# Run the application
root.mainloop()
