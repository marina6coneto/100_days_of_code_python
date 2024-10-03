
# Day 47: Amazon Price Alert

This Python script checks the price of a specific product on Amazon and sends an email alert when the price drops below a specified threshold. This project is a simple demonstration of web scraping using the Beautiful Soup library and email notifications using the smtplib library.

## Features

- Scrapes the price of a product from its Amazon page.
- Sends an email notification when the price drops below a defined limit.
- Uses environment variables to store sensitive information.

## Requirements

- Python 3.x
- `requests` library
- `beautifulsoup4` library
- `python-dotenv` library

You can install the required libraries using pip:

```bash
pip install requests beautifulsoup4 python-dotenv
```

## Environment Variables

Create a `.env` file in the root directory of the project to store your email credentials and SMTP server details. Here’s an example of what your `.env` file should look like:

```
EMAIL_ADDRESS=your_email@example.com
EMAIL_PASSWORD=your_email_password
SMTP_ADDRESS=smtp.example.com
```

Make sure to replace `your_email@example.com`, `your_email_password`, and `smtp.example.com` with your actual email credentials.

## How to Use

1. **Clone the repository**:

   ```bash
   git clone https://github.com/marina6coneto/100_days_of_code_python
  
   ```

2. **Run the script**:

   Open a terminal and execute the following command:

   ```bash
   python main.py
   ```

3. The script will scrape the price of the specified product and send an email alert if the price is below your defined threshold.

## Customize

You can customize the `BUY_PRICE` variable in the script to set your desired price threshold. Modify the `url` variable to check different products.

## Disclaimer

Please ensure that your web scraping activities comply with the website's terms of service. The author is not responsible for any violations resulting from the use of this script.
