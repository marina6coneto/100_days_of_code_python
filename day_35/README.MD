# Day_35: Weather Notification Project

This project is a weather notification system that checks if it's going to rain based on your location and sends an SMS alert using the Twilio API.

## Project Overview

This Python project fetches weather data from an external API and checks if rain is expected within the next few hours. If rain is predicted, the system sends an SMS reminder to bring an umbrella, using Twilio's SMS API.

## Features

- Fetches weather data based on geographical coordinates.
- Sends SMS notifications if rain is predicted.
- Uses Twilio API to handle the SMS sending.

## Technologies Used

- **Python**: Core programming language.
- **Requests**: Used to send HTTP requests to the weather API.
- **Twilio**: Service to send SMS notifications.
- **OpenWeatherMap API**: Provides weather data.

## Setup and Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/weather-notification.git
   cd weather-notification
   ```

2. **Install the required Python packages**:
   Make sure to have `requests` and `twilio` installed.
   ```bash
   pip install requests twilio
   ```

3. **Create an account on Twilio** and get the following credentials:
   - Account SID
   - Auth Token
   - Twilio Phone Number

4. **Sign up for an OpenWeatherMap account** and get an API key.

5. **Update the following variables in the code** with your details:
   - `own_endpoint`
   - `api_key`
   - `account_sid`
   - `auth_token`
   - `MY_LAT`
   - `MY_LON`
   - `from_` (Twilio phone number)
   - `to` (Your phone number)

## How to Run the Project

1. Ensure your internet connection is active.
2. Run the script:
   ```bash
   python weather_notification.py
   ```
3. If rain is predicted in the coming hours, you will receive an SMS notification.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
