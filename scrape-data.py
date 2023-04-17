from bs4 import BeautifulSoup as bs
import requests
import pandas as pd
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options

import time
# import matplotlib.pyplot as plt

geckodriver_path = '/Users/elliottweeks/nflWinnerProject/nflWinnerProject/geckodriver'

#This is the setup for the chrome driver, the options, and the url that we want to scrape
url = 'https://www.pro-football-reference.com/years/2022/index.htm'
response = requests.get(url)

options = Options()
# options.add_argument('--ignore-certificate-errors')
# options.add_argument('--incognito')
options.add_argument("-install-global-extension,/path/to/ublock-origin.xpi")
options.headless = True



# add the Firefox incognito mode alternative
options.set_preference("browser.privatebrowsing.autostart", True)

driver = webdriver.Firefox(options=options, executable_path=geckodriver_path)
driver.get('https://www.pro-football-reference.com/years/2022/index.htm')




#This is the while loop that our code sits in. It is counting down by year, and we are scraping ~something~ from every winning team

x=2022


while (x>2001):
    
    
    #finding the winning teams page
    teamPage = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[1]/div[2]/p[1]/a')  #Finds winning team element
    
    #This is the if statement that will clicks the next page and makes a soup object of the html
    if teamPage:
        teamPage.click()
        pageSource = driver.page_source
        soup = bs(driver.page_source, 'lxml')
    
    
    #finds the team stats table
    teamStats = soup.find('table', id='team_stats')
    

    # extract the data from the table using Pandas
    df = pd.read_html(str(teamStats),header=0)[0] 

    csvFileName=str(x)+'_team_stats.csv'
    df.to_csv(csvFileName,header=0,index=False)

    driver.back()
    lastYear=driver.find_element(By.XPATH, "//a[@class='button2 prev']")
    if lastYear:
        lastYear.click()
    x=x-1




driver.quit()