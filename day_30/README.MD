# Day 30: Password Manager 

- This is an enhanced Password Manager application built using Python and Tkinter.
- The application not only generates and saves strong passwords but also allows you to search for previously saved passwords using a JSON file for storage.
- This project is part of the "100 Days of Code: The Complete Python Pro Bootcamp" by Angela Yu on Udemy.

## Features

- **Password Generation**: Generates a strong, random password consisting of letters, numbers, and symbols.
- **Password Saving**: Saves the website, email/username, and password combination to a JSON file for secure storage.
- **Password Search**: Retrieves the saved password for a specific website.
- **Clipboard Copy**: Automatically copies the generated password to your clipboard for quick use.

## How to Run the Project

1. **Install Dependencies**: Ensure you have Python installed on your machine.
2. **Clone the Repository**: Clone this repository to your local machine.
3. **Run the Application**: Execute the Python script using a Python interpreter.
   ```bash
   python main.py
   ```
4. **Generate, Save, and Search Passwords**: Use the interface to generate, save, and manage your passwords.

## Usage

1. **Website**: Enter the name of the website for which you want to save or search the password.
2. **Email/Username**: Enter your email or username associated with the website.
3. **Generate Password**: Click the "Generate Password" button to create a strong password.
4. **Add Password**: Click the "Add" button to save the website, email/username, and password combination.
5. **Search Password**: Click the "Search" button to find the saved password for the entered website.
6. **Save Location**: The passwords are stored in a `data.json` file located in the `day_30` directory.

## Notes

- If a website already exists in the `data.json` file, the new entry will update the existing one.
- Ensure the `data.json` file is in the correct directory, or the application will create a new file if it doesn't exist.

*This project is part of the "100 Days of Code: The Complete Python Pro Bootcamp" by Angela Yu on Udemy*
