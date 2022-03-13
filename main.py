from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import  Keys
import time
import datetime
Cursor = 15
GRANDMA = 100
FACTORY = 500


def skill_click(clicks,driver):
    clicks = clicks.replace(",",'')
    clicks = int(clicks)
    if clicks>FACTORY:
        driver.find_element(By.ID,"buyFactory").click()
        return
    elif clicks>GRANDMA:
        driver.find_element(By.ID,"buyGrandma").click()
        return
    elif clicks>Cursor:
        driver.find_element(By.ID,"buyCursor").click()
        return
    else:
        return


cookie = True

service = Service("D:\Downloads\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get("http://orteil.dashnet.org/experiments/cookie")

the_cookie = driver.find_element(By.ID ,"cookie")

# 5 minutes from now
time_in_five_minutes=datetime.datetime.now() + datetime.timedelta(0,300)
start_time = datetime.datetime.now()

while cookie:
    if time_in_five_minutes == start_time:
        bool = False
    time_delta_five_sec = datetime.datetime.now()-start_time
    if time_delta_five_sec.total_seconds()>= 3:
        cookie_number = driver.find_element(By.ID, "money").text
        skill_click(cookie_number,driver)
        start_time = datetime.datetime.now()
    else:
        time.sleep(0.02)
        the_cookie.click()







