# Day 32: Birthday Wisher Project

- This project is a simple automation script that sends personalized birthday wishes via email. 
- It checks a CSV file containing birthday data and matches it with the current date.
- If it's someone's birthday, the program randomly selects a birthday letter template, customizes it with the person's name, and sends the email.
- *This project is part of the "100 Days of Code: The Complete Python Pro Bootcamp" by Angela Yu on Udemy.*

## Project Structure

The project has the following structure:


├── day_32

│   ├── birthday.csv

│   ├── letter_templates

│   │   ├── letter_1.txt

│   │   ├── letter_2.txt

│   │   └── letter_3.txt

└── main.py


- **`birthday.csv`**: This CSV file contains the list of birthdays with the columns: `name`, `email`, `year`, `month`, and `day`.
- **`letter_templates`**: This folder contains three letter templates (`letter_1.txt`, `letter_2.txt`, `letter_3.txt`). Each template includes a placeholder `[NAME]` that will be replaced by the recipient's name.
- **`main.py`**: The main Python script that performs the birthday checking and email sending.

## How It Works

1. The program checks today's date using Python's `datetime` module.
2. It reads the `birthday.csv` file to get the birthdays of various individuals.
3. If today's date matches any birthday in the CSV, it selects a random letter from the `letter_templates` folder.
4. The program replaces the placeholder `[NAME]` in the letter template with the birthday person's name.
5. Finally, it sends the personalized email to the birthday person using Gmail's SMTP service.

## Prerequisites

- Python 3.x
- Required Python packages:
  - `smtplib`
  - `pandas`
  - `datetime`
  - `random`

You can install the required packages using pip:

```bash
pip install pandas




