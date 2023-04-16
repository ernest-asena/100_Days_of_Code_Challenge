# If you need some info on the concept of web scraping, please read the notes file

# We will first scrap a live website, combinator hacker news (https://news.ycombinator.com/). We try to find the
# article with the largest number of upvotes from the page now, and print it together with a link to it
import requests
from bs4 import BeautifulSoup
base_url = 'https://news.ycombinator.com/'

page_html = requests.get(base_url)      # Get the html file defining the web page
page_text = page_html.text
soup = BeautifulSoup(page_text, 'lxml')    # Create a soup object specifying the parser to be used

# print(soup.prettify())
articles = soup.find_all(name='a', class_='titlelink')
# print(articles)
article_texts = []
article_links = []
for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(text)
    link = article_tag.get("href")
    article_links.append(link)

upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]
largest_number = max(upvotes)
largest_index = upvotes.index(largest_number)

print(article_texts[largest_index])
print(article_links[largest_index])


















