from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_driver_path = '/Users/nesi/dvm/chromedriver'
# base_url = 'https://en.wikipedia.org/wiki/Main_Page'
#
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)
# driver.get(url=base_url)
#
# # stat_number = driver.find_element(By.CSS_SELECTOR, value="#articlecount a")
# # stat_number.click()
#
# all_portals = driver.find_element(By.LINK_TEXT, 'All portals')
# # all_portals.click()
#
# search = driver.find_element(By.NAME, value='search')
# search.send_keys('Python')
# search.send_keys(Keys.ENTER)

driver.get('http://secure-retreat-92358.herokuapp.com/')

fname = driver.find_element(By.NAME, value='fName')
fname.send_keys('The Great')
lname = driver.find_element(By.NAME, value='lName')
lname.send_keys('Coding Monkey')
email = driver.find_element(By.NAME, value='email')
email.send_keys('TheGreatCodingMonkey@thegreatmail.com')
sign_up_button = driver.find_element(By.XPATH, value='/html/body/form/button')
sign_up_button.click()
sign_up_button = driver.find_element(By.CSS_SELECTOR, value="form button")
sign_up_button.click()







# driver.quit()
