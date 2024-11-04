# Weight Converter
A simple and efficient GUI-based Weight Converter application developed with Python and Tkinter. This app allows users to convert weight values between different units, including kilograms, grams, pounds, and ounces.

## Project Overview

This Weight Converter application enables users to easily convert between various weight units. The user inputs a weight value and selects both input and output units from dropdown menus, and the app instantly performs the conversion upon pressing the Convert button. The result is displayed in real-time, making it an intuitive tool for everyday conversions.

## Table of Contents
1. [Features](#Features)
2. [Requirements](#Requirements)
3. [Installation and Usage](#Installation#and#Usage)
4. [Code Explanation](#Code#Explanation)
5. [App Interface](#App#Interface)
6. [License](#License)

## Features
- **Unit Conversion:** Supports conversions between kilograms, grams, pounds, and ounces.
- **Intuitive Interface:** Provides easy input and selection of units, with the output displayed clearly.
- **Error Handling:** Handles invalid inputs gracefully with error messages.
- **Real-Time Calculation:** Converts instantly upon pressing the Convert button.

## Requirements
- Python 3.x
- Tkinter: Tkinter is the standard GUI library in Python, typically included with most Python installations.

## Installation and Usage
To use this Weight Converter application, follow these steps:

1. Clone the repository or copy the provided code.

2. Ensure Python is installed on your system.
3. Run the script using the command:
```bash
python conv.py
```
4. The GUI will open, allowing you to enter a weight value, select the input and output units, and press Convert to see the converted weight.

## Code Explanation
The app’s core functionality is driven by a set of conversion factors and a convert() function that performs the following steps:

1. **Retrieve Input:** Fetches the user’s input weight and selected units.
2. **Convert to Kilograms:** Converts the input weight to a baseline unit (kilograms).
3. **Convert to Target Unit:** Converts the weight in kilograms to the selected output unit.
4. **Display Result:** Updates the result label with the converted weight value in the desired unit.

### Conversion Factors
The conversion factors are defined for four common weight units:

```bash
conversion_factors = {
    "Kilogram (kg)": 1,
    "Gram (g)": 0.001,
    "Pound (lb)": 0.453592,
    "Ounce (oz)": 0.0283495
}
```

## Exception Handling
The **convert()** function includes exception handling to ensure the app gracefully manages any invalid inputs, such as non-numeric values.

## App Interface
Below is an image of the Weight Converter **GUI:**
![alt text](https://github.com/AhmedEssam29/Weight_Converter/blob/main/app.png?raw=true)

