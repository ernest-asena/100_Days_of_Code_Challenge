import requests
from bs4 import BeautifulSoup
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import config
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException

headers = {
    'Accept-Language': 'en-US,en;q=0.9,nl;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/95.0.4638.69 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,'
              'application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': 'gzip, deflate'

}

base_url = 'https://www.zillow.com/los-angeles-ca/rentals/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C' \
           '%22usersSearchTerm%22%3A%22Los%20Angeles%2C%20CA%22%2C%22mapBounds%22%3A%7B%22west%22%3A-118' \
           '.87590536328125%2C%22east%22%3A-117.94756063671875%2C%22south%22%3A33.69021528257619%2C%22north%22%3A34' \
           '.35151994648387%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A12447%2C%22regionType%22%3A6%7D%5D%2C' \
           '%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22min%22%3A0%2C%22max%22%3A872627%7D' \
           '%2C%22mp%22%3A%7B%22min%22%3A0%2C%22max%22%3A3000%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22ah%22%3A%7B' \
           '%22value%22%3Atrue%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C' \
           '%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value' \
           '%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%7D%2C' \
           '%22isListVisible%22%3Atrue%7D '
response = requests.get(url=base_url, headers=headers).text
soup = BeautifulSoup(response, 'lxml')

all_link_elements = soup.select(".list-card-top a")

all_links = []
for link in all_link_elements:
    href = link["href"]
    # print(href)
    if "https" not in href:
        all_links.append(f"https://www.zillow.com/homedetails{href}")
    else:
        all_links.append(href)

price_list = []
prices = soup.find_all(name='div', class_='list-card-price')
for price in prices:
    price.text.split('/')
    price.text.split('+')[0]
    price_list.append(price.text.split('+')[0])


# all_address_elements = soup.select(".list-card-info address")
# all_addresses = [address.get_text().split(" | ")[-1] for address in all_address_elements]
address_list = []
addresses = soup.find_all(name='address', class_='list-card-addr')
for address in addresses:
    address_list.append(address.text)

print(address_list)
print(price_list)
print(all_links)
#

#
chrome_driver_path = '/Users/nesi/dvm/chromedriver'
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)
driver.get(url=config.forms_url)

time.sleep(5)
for i in range(len(all_links)):
    adrs_field = driver.find_element(By.XPATH,
                                     value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    adrs_field.send_keys(address_list[i])

    price_field = driver.find_element(By.XPATH,
                                      value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price_field.send_keys(price_list[i])

    link_field = driver.find_element(By.XPATH,
                                     value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link_field.send_keys(all_links[i])

    submit_btn = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
    submit_btn.click()
    time.sleep(3)

    submit_another_response_btn = driver.find_element(By.XPATH, value='/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
    submit_another_response_btn.click()
    time.sleep(5)
