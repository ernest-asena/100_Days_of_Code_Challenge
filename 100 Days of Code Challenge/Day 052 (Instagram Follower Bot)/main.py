import config
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import ElementClickInterceptedException


class InstaFollower:
    """A bot that follows the followers of a given account"""
    def __init__(self):
        """Initializes the bot"""
        self.chrome_driver_path = '/Users/nesi/dvm/chromedriver'
        self.service = Service(self.chrome_driver_path)
        self.driver = webdriver.Chrome(service=self.service)

    def login(self):
        """Logs in to Instagram"""
        self.driver.get(url='https://www.instagram.com/')
        time.sleep(20)
        mail_field = self.driver.find_element(By.XPATH, value='//*[@id="loginForm"]/div/div[1]/div/label/input')
        mail_field.send_keys(config.INSTAGRAM_MAIL)
        passwd_field = self.driver.find_element(By.XPATH, value='//*[@id="loginForm"]/div/div[2]/div/label/input')
        passwd_field.send_keys(config.INSTAGRAM_PASS)
        login_btn = self.driver.find_element(By.XPATH, value='//*[@id="loginForm"]/div/div[3]/button')
        login_btn.click()
        time.sleep(20)
        not_now = self.driver.find_element(By.XPATH, value='//*[@id="react-root"]/section/main/div/div/div/div/button')
        not_now.click()
        time.sleep(60)
        not_now_for_notifications = self.driver.find_element(By.XPATH,
                                                             value='/html/body/div[5]/div/div/div/div[3]/button[2]')
        not_now_for_notifications.click()
        time.sleep(30)

    def find_followers(self):
        """Finds the followers of a given account"""
        time.sleep(30)
        self.driver.get(f"https://www.instagram.com/{config.INSTAGRAM_TO_SEARCH}")

        time.sleep(15)
        followers = self.driver.find_element(By.XPATH,
                                             value='//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
        followers.click()

        time.sleep(30)
        modal = self.driver.find_element(By.XPATH, value='/html/body/div[6]/div/div')
        for i in range(256):

            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(2)

    def follow(self):
        """Follows all the followers of a given account"""
        all_buttons = self.driver.find_elements(By.CSS_SELECTOR, value="li button")
        for button in all_buttons:
            try:
                button.click()
                time.sleep(2)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(By.XPATH, value='/html/body/div[5]/div/div/div/div['
                                                                         '3]/button[2]')
                cancel_button.click()
        self.driver.quit()


bot = InstaFollower()
bot.login()
bot.find_followers()
bot.follow()
