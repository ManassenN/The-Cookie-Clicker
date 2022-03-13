from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import  Keys

service = Service("D:\Downloads\chromedriver_win32\chromedriver")
driver = webdriver.Chrome(service = service)

driver.get("https://en.wikipedia.org/wiki/Main_Page")



# article_count = driver.find_element(By.CSS_SELECTOR,'#articlecount a')
# article_count.click()
# print(article_count.text)


search = driver.find_element(By.NAME,'search')
search.send_keys('Python')

# clicking the button
driver.find_element(By.CSS_SELECTOR, '#searchButton').click()






# driver.close()
