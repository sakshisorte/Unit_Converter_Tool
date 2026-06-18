import tkinter as tk
from tkinter import ttk, messagebox

def convert():
    try:
        value = float(entry_value.get())

        category = combo_category.get()
        from_unit = combo_from.get()
        to_unit = combo_to.get()

        result = 0

        # Length
        if category == "Length":
            length_units = {
                "Meter": 1,
                "Kilometer": 1000,
                "Centimeter": 0.01
            }

            result = value * length_units[from_unit] / length_units[to_unit]

        # Weight
        elif category == "Weight":
            weight_units = {
                "Gram": 1,
                "Kilogram": 1000
            }

            result = value * weight_units[from_unit] / weight_units[to_unit]

        # Temperature
        elif category == "Temperature":

            if from_unit == "Celsius" and to_unit == "Fahrenheit":
                result = (value * 9/5) + 32

            elif from_unit == "Fahrenheit" and to_unit == "Celsius":
                result = (value - 32) * 5/9

            else:
                result = value

        lbl_result.config(text=f"Result: {round(result,2)}")

    except:
        messagebox.showerror("Error", "Enter Valid Number")

def update_units(event=None):

    category = combo_category.get()

    if category == "Length":
        units = ["Meter", "Kilometer", "Centimeter"]

    elif category == "Weight":
        units = ["Gram", "Kilogram"]

    elif category == "Temperature":
        units = ["Celsius", "Fahrenheit"]

    combo_from['values'] = units
    combo_to['values'] = units

    combo_from.current(0)
    combo_to.current(1)

root = tk.Tk()
root.title("Unit Converter Tool")
root.geometry("450x350")

title = tk.Label(root,text="UNIT CONVERTER TOOL",
                 font=("Arial",16,"bold"))
title.pack(pady=10)

tk.Label(root,text="Category").pack()

combo_category = ttk.Combobox(root,
                              values=["Length",
                                      "Weight",
                                      "Temperature"])
combo_category.pack()
combo_category.bind("<<ComboboxSelected>>", update_units)

tk.Label(root,text="Value").pack()
entry_value = tk.Entry(root)
entry_value.pack()

tk.Label(root,text="From Unit").pack()
combo_from = ttk.Combobox(root)
combo_from.pack()

tk.Label(root,text="To Unit").pack()
combo_to = ttk.Combobox(root)
combo_to.pack()

btn = tk.Button(root,text="Convert",
                command=convert)
btn.pack(pady=15)

lbl_result = tk.Label(root,
                      text="Result:",
                      font=("Arial",14))
lbl_result.pack()

combo_category.current(0)
update_units()

root.mainloop()