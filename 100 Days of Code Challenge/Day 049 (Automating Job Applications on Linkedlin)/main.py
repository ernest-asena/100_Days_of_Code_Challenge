from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import config
import time

chrome_driver_path = '/Users/nesi/dvm/chromedriver'
jobs_url = 'https://www.linkedin.com/jobs/search/?f_AL=true&geoId=101339379&keywords=data%20analyst&location=Nairobi%2C%20Kenya'

service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)
driver.get(url=jobs_url)

sign_in_button = driver.find_element(By.XPATH, value='/html/body/div[1]/header/nav/div/a[2]')
sign_in_button.click()

time.sleep(2)
email_field = driver.find_element(By.CSS_SELECTOR, value='#username')
email_field.send_keys(config.LINKEDLIN_USERNAME)

email_field = driver.find_element(By.CSS_SELECTOR, value='#password')
email_field.send_keys(config.LINKEDLIN_PASS)

sign_in_btn = driver.find_element(By.XPATH, value='//*[@id="organic-div"]/form/div[3]/button')
sign_in_btn.click()

time.sleep(5)
apply_now_button = driver.find_element(By.CSS_SELECTOR, value='.jobs-apply-button')
apply_now_button.click()

# If application requires phone number and the field is empty, then fill in the number.
time.sleep(5)
phone = driver.find_element(By.CLASS_NAME, value="fb-single-line-text__input")
if phone.text == "":
    phone.send_keys(config.LINKEDLIN_PHONE)

# Submit the application
submit_button = driver.find_element(By.CSS_SELECTOR, value="footer button")
submit_button.click()
