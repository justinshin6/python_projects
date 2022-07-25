from bs4 import BeautifulSoup
import requests 



URL = 'https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/'
DIRECTORY_FILE_PATH = 'top-100-movies-data/'

response = requests.get(URL)
empire_webpage = response.text

soup = BeautifulSoup(empire_webpage, 'html.parser')

# get all of the titles in the empire_webpage
titles_tags = soup.find_all(name='h3', class_='title')
all_titles = [''] * len(titles_tags)
# reverse the titles
for i in range(len(titles_tags) - 1, -1, -1):
    all_titles[len(titles_tags) - 1 - i] = titles_tags[i].getText()

# another syntax is the following to reverse the list of titles
# movies = all_titles[::-1]

# open up a new text_file with the movie titles
with open(f'{DIRECTORY_FILE_PATH}movies.txt', mode='w') as file:
    # for each movie, print on a new line
    for movie in all_titles:
        file.write(f"{movie}\n")
