import requests
from bs4 import BeautifulSoup
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

url = '''https://www.amazon.com.br/Funko-Harry-Potter-Pop/dp/B076HVJN7T/ref=sr_1_3?__mk_pt_BR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&sr=8-3&ufe=app_do%3Aamzn1.fos.6d798eae-cadf-45de-946a-f477d47705b9'''


header = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-GB,de;q=0.8,fr;q=0.6,en;q=0.4,ja;q=0.2",
    "Dnt": "1",
    "Priority": "u=1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Sec-Gpc": "1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:126.0) Gecko/20100101 Firefox/126.0",
}

response = requests.get(url, headers=header)

soup = BeautifulSoup(response.text, 'html.parser')


price = soup.find('span', class_='a-offscreen').get_text()

price_without_currency = price.replace('R$', '').replace(',', '.').strip()

price_as_float = float(price_without_currency)

# ---------------------------- SEND EMAIL ------------------------------- #

title = soup.find(id = 'productTitle').get_text().strip()
 
BUY_PRICE = 162

if price_as_float < BUY_PRICE:
    message = f"{title} is on sale for {price_as_float}! Buy it now!"
    
    with smtplib.SMTP(os.environ['SMTP_ADDRESS'], port=587) as connection:
        connection.starttls()
        result = connection.login(os.environ['EMAIL_ADDRESS'], os.environ['EMAIL_PASSWORD'])
        connection.sendmail(
            from_addr=os.environ['EMAIL_ADDRESS'],
            to_addrs=os.environ['EMAIL_ADDRESS'],
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}".encode('utf-8')
        )
    