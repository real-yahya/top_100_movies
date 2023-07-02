import requests
from bs4 import BeautifulSoup

URL = 'https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/'
response = requests.get(URL)
web_data = response.text

soup = BeautifulSoup(web_data, 'html.parser')
movies = soup.findAll(
    'h3', class_="title")

movie_list = [movie.getText() for movie in movies]
movie_list.reverse()

with open('Top 100 movies.txt', 'w') as file:
    for i in movie_list:
        file.write(i+'\n')
