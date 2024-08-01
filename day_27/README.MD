# Day 27: Miles to KM Converter

- This project is part of the "100 Days of Code: Python" course by Angela Yu. 
- This is a simple graphical user interface (GUI) application built using Tkinter in Python.
- The application converts a distance in miles to kilometers.

## Description

- The application takes an input in miles, converts it to kilometers, and displays the result.
- It handles invalid inputs gracefully by displaying an error message.

## How It Works

1. The user enters a distance in miles into the input field.
2. When the "Calculate" button is clicked, the application converts the distance to kilometers and displays the result.

## Code Explanation

- **Tkinter** is used to create the GUI.
- **Entry** widget is used to get the user's input.
- **Label** widgets are used to display text in the GUI.
- **Button** widget is used to trigger the conversion.
- The conversion is handled by the `miles_to_km` function, which is called when the button is clicked.

## Function

- `miles_to_km()`: This function retrieves the value from the input field, converts it to kilometers, and updates the result label.
- If the input is not a valid number, it displays an error message.

## How to Run the Project

1. Make sure you have Python installed on your computer.
2. Save the code in a file with a `.py` extension, for example, `miles_to_km_converter.py`.
3. Open a terminal or command prompt.
4. Navigate to the directory where the file is saved.
5. Run the script using the command: `python miles_to_km_converter.py`.
