# scrapper to get list of 100 best movies of all time from https://www.empireonline.com/movies/features/best-movies-2/

import requests
from bs4 import BeautifulSoup

base_url = 'https://www.empireonline.com/movies/features/best-movies-2/'
response = requests.get(url='https://www.empireonline.com/movies/features/best-movies-2/')
response_text = response.text

soup = BeautifulSoup(response_text, 'lxml')

print(soup.prettify())

all_movies = soup.find_all(name="h3", class_="jsx-4245974604")

movie_titles = [movie.getText() for movie in all_movies]
movies = movie_titles[::-1]

# with open("movies.txt", mode="w") as file:
#     for movie in movies:
#         file.write(f"{movie}\n")
