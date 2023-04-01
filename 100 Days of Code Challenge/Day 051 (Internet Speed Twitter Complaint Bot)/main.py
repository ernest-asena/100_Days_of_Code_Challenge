from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import config
import time
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException

PROMISED_UP = 10
PROMISED_DOWN = 5
TWITTER_EMAIL = config.TWITTER_EMAIL
TWITTER_PASS = config.TWITTER_PASS


class InternetSpeedTwitterBot:
    """A bot that tweets at your internet provider when your internet speed is below the promised speed"""
    def __init__(self):
        """Initialize the bot"""
        self.chrome_driver_path = '/Users/nesi/dvm/chromedriver'
        self.up = 10
        self.down = 5

    def get_internet_speed(self):
        """Gets the internet speed from fast.com"""
        service = Service(self.chrome_driver_path)
        driver = webdriver.Chrome(service=service)
        driver.get(url='https://www.fast.com/')
        time.sleep(50)
        speed = float(driver.find_element(By.CSS_SELECTOR, value='#speed-value').text)
        return speed

    def tweet_at_provider(self):
        """Tweets at your internet provider when your internet speed is below the promised speed"""
        service = Service(self.chrome_driver_path)
        driver = webdriver.Chrome(service=service)
        driver.get(url='https://twitter.com/')
        time.sleep(25)

        sign_in_btn = driver.find_element(By.XPATH,
                                          value='//*[@id="react-root"]/div/div/div/main/div/div/div/div[1]/div/div[3]/div[4]/span/span')
        sign_in_btn.click()
        time.sleep(15)

        mail_sign_in = driver.find_element(By.XPATH,
                                           value='//*[@id="react-root"]/div/div/div/main/div/div/div/div[1]/div/div[3]/a')
        mail_sign_in.click()
        time.sleep(10)

        mail_field = driver.find_element(By.XPATH,
                                         value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label')
        mail_field.send_keys(config.TWITTER_EMAIL)
        time.sleep(10)

        next_btn = driver.find_element(By.XPATH,
                                       value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div')
        next_btn.click()
        time.sleep(15)

        phone_no_field = driver.find_element(By.XPATH,
                                             value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input')
        phone_no_field.send_keys(config.TWITTER_PHONE)
        time.sleep(5)

        next_btn = driver.find_element(By.XPATH,
                                       value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div')
        next_btn.click()
        time.sleep(10)

        passwd_field = driver.find_element(By.XPATH,
                                           value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[3]/div/label/div/div[2]/div/input')
        passwd_field.send_keys(config.TWITTER_PASS)
        time.sleep(6)

        log_in_btn_final = driver.find_element(By.XPATH,
                                               value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div')
        log_in_btn_final.click()
        time.sleep(6)

        new_tweet_btn = driver.find_element(By.XPATH,
                                            value='//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a')
        new_tweet_btn.click()
        time.sleep(10)

        new_tweet_field = driver.find_element(By.XPATH,
                                              value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[3]/div/div/div/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div')
        new_tweet_field.send_keys(f"Hey @Zuku_WeCare. I am getting only {speed}Mbps Up!!\n You promised {PROMISED_DOWN}Mbps!!")
        send_tweet_btn = driver.find_element(By.XPATH,
                                             value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[3]/div/div/div/div[1]/div/div/div/div/div[2]/div[3]/div/div/div[2]/div[4]')
        send_tweet_btn.click()
        time.sleep(30)


bot = InternetSpeedTwitterBot()

speed = bot.get_internet_speed()
print(speed)

if speed < PROMISED_DOWN:
    bot.tweet_at_provider()

