from tkinter import *

# Conversion factors from each unit to kilograms
conversion_factors = {
    "Kilogram (kg)": 1,
    "Gram (g)": 0.001,
    "Pound (lb)": 0.453592,
    "Ounce (oz)": 0.0283495
}

# Function to perform the conversion based on selected units
def convert():
    try:
        input_value = float(e2_value.get())
        # Convert input to kilograms
        kg_value = input_value * conversion_factors[input_unit.get()]
        # Convert from kilograms to the target output unit
        converted_value = kg_value / conversion_factors[output_unit.get()]
        
        # Update the result label with the converted value
        result_label.config(text=f"{converted_value:.2f} {output_unit.get().split()[1]}")
    except ValueError:
        result_label.config(text="Invalid input")

# Initialize the window
window = Tk()
window.title("Weight Converter")

# Input label and entry
e1 = Label(window, text="Input the weight:")
e1.grid(row=0, column=0)

e2_value = StringVar()
e2 = Entry(window, textvariable=e2_value)
e2.grid(row=0, column=1)

# Dropdown menu for selecting the input unit
input_unit = StringVar(window)
input_unit.set("Kilogram (kg)")  # default value
input_menu = OptionMenu(window, input_unit, *conversion_factors.keys())
input_menu.grid(row=0, column=2)

# Dropdown menu for selecting the output unit
output_unit = StringVar(window)
output_unit.set("Gram (g)")  # default value
output_menu = OptionMenu(window, output_unit, *conversion_factors.keys())
output_menu.grid(row=1, column=2)

# Output label to display the result
result_text = Label(window, text="Converted weight:")
result_text.grid(row=1, column=0)

result_label = Label(window, text="")
result_label.grid(row=1, column=1)

# Convert button
convert_button = Button(window, text="Convert", command=convert)
convert_button.grid(row=2, column=1)

# Run the application
window.mainloop()
