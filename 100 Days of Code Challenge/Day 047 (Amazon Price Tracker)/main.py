import requests
from bs4 import BeautifulSoup
import smtplib
import config

item_url = 'https://www.amazon.com/Apple-MacBook-2-5GHz-MGXC2LL-Refurbished/dp/B0784J8FXM/ref=sr_1_2?dchild=1' \
           '&keywords=macbook+pro+15+inch&qid=1635619549&sr=8-2'

headers = {
    'Accept-Language': 'en-US,en;q=0.9,nl;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/95.0.4638.69 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,'
              'application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': 'gzip, deflate'

}

page_html = requests.get(url=item_url, headers=headers)
page_text = page_html.text

soup = BeautifulSoup(page_text, 'html.parser')
item_price = soup.find(name="span", id='price_inside_buybox')
# print(item_price.getText())
price = item_price.getText()
price_split = float(price.split('$')[1])
print(price_split)

# if price_split <= 750:
#     with smtplib.SMTP('smtp.gmail.com') as connection:
#         connection.starttls()
#         connection.login(user=config.my_email, password=config.password)
#         connection.sendmail(from_addr=config.my_email, to_addrs=config.EMAIL_MAIN,
#                             msg=F"Subject: YOUR MACBOOK PRICE DOWN!!\n\nErnest, Your Favorite Mac's Price Went "
#                                 F"Down.\n\nThe Price is now ${price_split}\n\nHurry Up Now!Here's the link to buy it: {item_url}\n\nRegards,\nYour "
#                                 F"Favorite Bot!")
