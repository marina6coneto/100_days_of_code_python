
# Day 38: Exercise Tracker with Nutritionix API and Google Sheets Integration

This Python script allows you to track your exercises by integrating with the Nutritionix API. It records the exercises you perform, along with their duration and calories burned, and logs them into a Google Sheet.

## Features
- Input your daily exercises and track details such as exercise name, duration, and calories burned.
- Connects to the [Nutritionix API](https://www.nutritionix.com/business/api) to fetch exercise data.
- Automatically logs exercise details into a Google Sheet via a specified API endpoint.
- Uses environment variables to securely store sensitive data such as API keys and credentials.

## Requirements
To run this project, you'll need the following:
- Python 3.x
- Required Python packages (see below for installation)
- Nutritionix API credentials (APP_ID and API_KEY)
- Google Sheets API endpoint and credentials (SHEET_ENDPOINT, USERNAME, PASSWORD)

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/marina6coneto/100_days_of_code_python/tree/master/day_38.git
   cd yourrepository
   ```

2. **Install required Python libraries**:
   Ensure you have `requests` installed. You can install it using pip:
   ```bash
   pip install requests
   ```

## Setup

1. **Set up environment variables**:
   You need to set the following environment variables on your system for the script to work. You can set these in your operating system or use a `.env` file with a library like `python-dotenv` to load them.

   - `APP_ID`: Your Nutritionix API App ID
   - `API_KEY`: Your Nutritionix API Key
   - `SHEET_ENDPOINT`: The endpoint URL for your Google Sheet API
   - `USERNAME`: Your username for authentication with the Google Sheets API
   - `PASSWORD`: Your password or token for authentication with the Google Sheets API

   For example, in a Unix-based system, you can set environment variables by running:

   ```bash
   export APP_ID=your_app_id
   export API_KEY=your_api_key
   export SHEET_ENDPOINT=your_sheet_endpoint
   export USERNAME=your_username
   export PASSWORD=your_password
   ```

2. **Run the script**:
   After setting the environment variables, you can run the script as follows:
   ```bash
   python main.py
   ```

3. **Input your exercises**:
   When prompted, input the exercises you performed. The script will fetch the relevant exercise data from Nutritionix and log it into the Google Sheet.

## Notes
- Ensure your environment variables are set correctly, as the script will not work without valid credentials and API keys.
- The Nutritionix API will require a valid APP_ID and API_KEY for authorization.
- The Google Sheets endpoint should be set up correctly to accept POST requests for logging workout data.
