from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import config
import time
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException


chrome_driver_path = '/Users/nesi/dvm/chromedriver'
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)
driver.get(url='https://tinder.com')

time.sleep(10)
log_in_btn = driver.find_element(By.XPATH, value='/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a')
log_in_btn.click()

time.sleep(10)
log_in_with_FB = driver.find_element(By.XPATH, value='//*[@id="q1750641709"]/div/div/div[1]/div/div[3]/span/div[2]/button')
log_in_with_FB.click()

time.sleep(10)
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
email_field = driver.find_element(By.XPATH, value='//*[@id="email"]')
email_field.send_keys(config.TINDER_FB)
passwd_field = driver.find_element(By.XPATH, value='//*[@id="pass"]')
passwd_field.send_keys(config.TINDERPASS)
# log_in_btn_fb = driver.find_element(By.CSS_SELECTOR, value='#loginbutton')
# log_in_btn_fb.click()
passwd_field.send_keys(Keys.ENTER)

driver.switch_to.window(base_window)

time.sleep(5)
allow_location_button = driver(By.XPATH, value='//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
allow_location_button.click()
notifications_button = driver(By.XPATH, value='//*[@id="modal-manager"]/div/div/div/div/div[3]/button[2]')
notifications_button.click()
cookies = driver(By.XPATH, value='//*[@id="content"]/div/div[2]/div/div/div[1]/button')
cookies.click()

for n in range(100):
    time.sleep(1)
    try:
        print("called")
        like_button = driver.find_element(By.XPATH, value='//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')

        like_button.click()
    except ElementClickInterceptedException:
        try:
            match_popup = driver.find_element_by_css_selector(".itsAMatch a")
            match_popup.click()
        except NoSuchElementException:
            time.sleep(2)

driver.quit()