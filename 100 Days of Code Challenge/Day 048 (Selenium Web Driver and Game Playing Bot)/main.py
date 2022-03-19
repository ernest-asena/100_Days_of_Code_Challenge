from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


chrome_driver_path = '/Users/nesi/dvm/chromedriver'
# driver = webdriver.Chrome(executable_path=chrome_driver_path)
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)
# driver.get(url='https://www.amazon.com/Apple-MacBook-2-5GHz-MGXC2LL-Refurbished/dp/B0784J8FXM/ref=sr_1_2?dchild=1&keywords=macbook+pro+15+inch&qid=1635619549&sr=8-2')
# driver.get(url='https://www.amazon.com/Apple-MacBook-2-5GHz-MGXC2LL-Refurbished/dp/B0784J8FXM/ref=sr_1_2?dchild=1&keywords=macbook%2Bpro%2B15%2Binch&qid=1635619549&sr=8-2&th=1')
# driver.maximize_window()
# price = driver.find_element(By.ID, value='price_inside_buybox')
# item_title = driver.find_element(By.XPATH, value='//*[@id="title"]')
# print(item_title.text)
# print()
# print(price.text)
# print()
# all_span_tags = driver.find_elements(By.TAG_NAME, value='span')
# for tag in all_span_tags:
#     print(tag.text)

# driver.close()


driver.get(url='https://www.speedtest.net/')
# time.sleep(5)
go_btn = driver.find_element(By.XPATH, value='/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a')
go_btn.click()
# driver.quit()