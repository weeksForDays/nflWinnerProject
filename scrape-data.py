from bs4 import BeautifulSoup as bs
import requests
import pandas as pd
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
import time
# import matplotlib.pyplot as plt

url = 'https://www.pro-football-reference.com/years/2022/index.htm'
response = requests.get(url)

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')

driver = webdriver.Chrome('C:\\Users\\Peter\\Desktop\\COS_Courses\\482\\Project\\chromedriver_win32\\chromedriver')
driver.get('https://www.pro-football-reference.com/years/2022/index.htm')

soup = bs(driver.page_source, 'lxml')

screen_height = driver.execute_script('return window.screen.height;')
i = 1.5

while True:
    driver.execute_script('window.scrollTo(0, {screen_height}*{i});'.format(screen_height=screen_height, i=i))
    i += 1
    time.sleep(3)

    scroll_height = driver.execute_script('return document.body.scrollHeight;')

    if (((screen_height) * i > scroll_height) or (i > 3)):
        break



nextPage = driver.find_element(By.XPATH, '//*[@id="playoff_results"]/tbody/tr[13]/td[3]/strong/a')

'/html/body/div[2]/div[5]/div[3]/div[3]/table/tbody/tr[11]/td[3]/strong/a'

# '//*[@id="playoff_results"]/tbody/tr[11]/td[3]/strong/a'

if nextPage:
    nextPage.click()
    pageSource = driver.page_source
    soup = bs(driver.page_source, 'lxml')


# all_item_info = soup.find_all('div', class_='item-info')