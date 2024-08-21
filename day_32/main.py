from smtplib import SMTP
from datetime import datetime
from random import randint 
from pandas import read_csv

##################### Birthday Wisher Project ######################


MY_EMAIL = 'mionegwp@gmail.com'
PASSWORD = 'mfrx fhso sdul iqad'


now = datetime.now()
today_day = now.day
today_month = now.month
today = (today_month, today_day)

file = read_csv('day_32/birthday.csv')

birthdays_dict = {(data_row['month'], data_row['day']): data_row for (index, data_row) in file.iterrows()}

if today in birthdays_dict:
    birthdays_person = birthdays_dict[today]
    file_path = f'day_32/letter_templates/letter_{randint(1,3)}.txt'
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace('[NAME]', birthdays_person['name'])
    with SMTP('smtp.gmail.com') as connection:
           connection.starttls()
           connection.login(user=MY_EMAIL, password=PASSWORD) 
           connection.sendmail(from_addr=MY_EMAIL,
                               to_addrs=birthdays_person['email'],
                               msg=f'Subject: Happy Birthday\n\n{contents}')


