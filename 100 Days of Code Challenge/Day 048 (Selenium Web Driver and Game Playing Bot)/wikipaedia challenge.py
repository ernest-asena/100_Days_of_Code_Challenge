from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_driver_path = '/Users/bond/devset/chromedriver'
base_url = 'https://en.wikipedia.org/wiki/Main_Page'

# Challenge; print out the 'statistics' number at the wikipedia page

service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)
driver.get(url=base_url)

# stat_number = driver.find_element(By.XPATH, value='//*[@id="articlecount"]/a[1]').text
# print(stat_number)

# OR
stat_number = driver.find_element(By.CSS_SELECTOR, value="#articlecount a").text
print(stat_number)

driver.quit()
