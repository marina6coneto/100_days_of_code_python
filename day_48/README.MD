# Day 48: Cookie Clicker Bot

This project is a simple bot for the Cookie Clicker game using Selenium in Python. The bot automates the process of clicking the cookie and purchasing upgrades to maximize the cookie production rate.

## Requirements

- Python 3.x
- Selenium
- Chrome WebDriver

## Installation

1. Install Selenium:
    ```bash
    pip install selenium
    ```

2. Download and install the Chrome WebDriver from [here](https://sites.google.com/a/chromium.org/chromedriver/downloads) and ensure it is in your system's PATH.

## Usage

1. Save the script to a file, e.g., `cookie_clicker_bot.py`.
2. Run the script:
    ```bash
    python cookie_clicker_bot.py
    ```

## How It Works

1. **Setup**: The script imports the necessary modules and sets up Chrome options to keep the browser open after execution.
2. **Initialization**: It initializes the Chrome driver and navigates to the Cookie Clicker game URL.
3. **Element Identification**: The script identifies the cookie element and the store items by their IDs.
4. **Main Loop**: 
    - The bot continuously clicks the cookie.
    - Every 5 seconds, it checks the available upgrades and purchases the most expensive one that can be afforded.
    - After 5 minutes, it prints the cookies per second rate and stops.

## Code

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=chrome_options)
driver.get('https://orteil.dashnet.org/experiments/cookie/')

cookie = driver.find_element(By.ID, value='cookie')
items = driver.find_elements(By.CSS_SELECTOR, value='#store div')
items_ids = [item.get_attribute('id') for item in items]

timeout = time.time() + 5
five_min = time.time() + 60*5

while True:
    cookie.click()

    if time.time() > timeout:
        all_prices = driver.find_elements(By.CSS_SELECTOR, value='#store b')
        item_prices = []

        for price in all_prices:
            element_text = price.text
            if element_text != '':
                cost = int(element_text.split('-')[1].strip().replace(',', ''))
                item_prices.append(cost)

        cookie_upgrades = {}
        for n in range(len(item_prices)):
            cookie_upgrades[item_prices[n]] = items_ids[n]

        money_element = driver.find_element(By.ID, value='money').text
        if ',' in money_element:
            money_element = money_element.replace(',', '')
        cookie_count = int(money_element)

        affordable_upgrades = {}
        for cost, id in cookie_upgrades.items():
            if cookie_count > cost:
                affordable_upgrades[cost] = id

        highest_price_affordable_upgrades = max(affordable_upgrades)
        print(highest_price_affordable_upgrades)
        to_purchase_id = affordable_upgrades[highest_price_affordable_upgrades]

        driver.find_element(By.ID, value=to_purchase_id).click()

        timeout = time.time() + 5

    if time.time() > five_min:
        cookie_per_s = driver.find_element(By.ID, value='cps').text
        print(cookie_per_s)
        break
```

## Notes

- Ensure that the Chrome WebDriver version matches your installed Chrome browser version.
- The script is designed to run for 5 minutes and then stop. You can adjust the `five_min` variable to change this duration.

Enjoy automating your Cookie Clicker game!