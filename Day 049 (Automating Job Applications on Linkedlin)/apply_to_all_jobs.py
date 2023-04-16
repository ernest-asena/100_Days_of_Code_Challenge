from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
import config

ACCOUNT_EMAIL = config.LINKEDLIN_USERNAME
ACCOUNT_PASSWORD = config.LINKEDLIN_PASS
PHONE = config.LINKEDLIN_PHONE


chrome_driver_path = '/Users/nesi/dvm/chromedriver'

service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)



jobs_url = 'https://www.linkedin.com/jobs/search/?f_AL=true&geoId=101339379&keywords=data%20analyst&location=Nairobi%2C%20Kenya'

driver.get(url=jobs_url)
time.sleep(2)
sign_in_button = driver.find_element(By.LINK_TEXT, value="Sign in")
sign_in_button.click()

time.sleep(5)
email_field = driver.find_element(By.ID, value="username")
email_field.send_keys(ACCOUNT_EMAIL)
password_field = driver.find_element(By.ID, value="password")
password_field.send_keys(ACCOUNT_PASSWORD)
password_field.send_keys(Keys.ENTER)

time.sleep(5)

all_listings = driver.find_elements(By.CSS_SELECTOR, value=".job-card-container--clickable")

for listing in all_listings:
    print("called")
    listing.click()
    time.sleep(2)
    try:
        apply_button = driver.find_element(By.CSS_SELECTOR, value=".jobs-s-apply button")
        apply_button.click()

        time.sleep(5)
        phone = driver.find_element(By.CLASS_NAME, value="fb-single-line-text__input")
        if phone.text == "":
            phone.send_keys(PHONE)

        submit_button = driver.find_element(By.CSS_SELECTOR, value="footer button")
        if submit_button.get_attribute("data-control-name") == "continue_unify":
            close_button = driver.find_element(By.CLASS_NAME, value="artdeco-modal__dismiss")
            close_button.click()

            time.sleep(2)
            discard_button = driver.find_elements(By.CLASS_NAME, value="artdeco-modal__confirm-dialog-btn")[1]
            discard_button.click()
            print("Skipped, Complex application.")
            continue
        else:
            submit_button.click()

        time.sleep(2)
        close_button = driver.find_element(By.CLASS_NAME, value="artdeco-modal__dismiss")
        close_button.click()

    except NoSuchElementException:
        print("No application button, skipped.")
        continue

time.sleep(5)
driver.quit()

