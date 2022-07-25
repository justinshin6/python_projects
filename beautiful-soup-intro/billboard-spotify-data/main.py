from bs4 import BeautifulSoup
import requests
import re

regex = re.compile("[0-9]{4}\-[0-1][0-9]\-[0-9]{2}")

def check_date_format(date):
    match = re.match(regex, date)

    if (match):
        return date

    else: 
       return check_date_format(input("Invalid date, try again: "))

user_input_data = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

print(check_date_format(user_input_data))

URL = f'https://www.billboard.com/charts/hot-100/{user_input_data}/'
response = requests.get(URL)
billboard_webpage = response.text

soup = BeautifulSoup(billboard_webpage, 'html.parser')

# get the titles from the BillBoard website
title_tags = soup.find_all(name='h3', id='title-of-a-story', class_='a-no-trucate')
titles = [title.getText().strip() for title in title_tags]
