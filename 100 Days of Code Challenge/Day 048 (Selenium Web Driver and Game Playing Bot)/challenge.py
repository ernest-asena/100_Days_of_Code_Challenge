from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Scrap the 'python.org' website for upcoming events and create a dictionary that has the dates and event names.

chrome_driver_path = '/Users/nesi/dvm/chromedriver'
url = 'https://www.python.org/'

service = Service(chrome_driver_path)

driver = webdriver.Chrome(service=service)

driver.get(url=url)

times = driver.find_elements(By.CSS_SELECTOR, value=".medium-widget event-widget last, .icon-calendar,  time")
events = driver.find_elements(By.CSS_SELECTOR, value=".medium-widget event-widget last, .icon-calendar, li, a")
for time in times:
    print(time.text)
    print()
for event in events:
    print(event.text)

# tis = driver.find_elements(By.XPATH, '//*[@id="content"]/div/section/div[3]/div[2]')
# print(tis)
# for i in tis:
#     print(i.text)
#     print(type(i))


driver.quit()
