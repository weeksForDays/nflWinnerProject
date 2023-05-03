from bs4 import BeautifulSoup as bs
import requests
import pandas as pd
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import ElementClickInterceptedException

import time
# import matplotlib.pyplot as plt


def main():


    url = 'https://www.pro-football-reference.com/years/2022/index.htm'
    response = requests.get(url)

    options = Options()
    # options.add_argument('--ignore-certificate-errors')
    # options.add_argument('--incognito')
    # options.add_argument("-install-global-extension,/Users/elliottweeks/nflWinnerProject/uBlock0_1.48.8.firefox.xpi")
    

    # add the Chrome incognito mode alternative
    options.add_argument("--incognito")
    options.add_argument("--start-maximized")

    #options.add_argument("--headless")

    # Set the path to the Chrome driver executable
    chromedriver_path = '/Users/elliottweeks/nflWinnerProject/nflWinnerProject/chromedriver_mac64/chromedriver'

    driver = webdriver.Chrome(options=options, executable_path=chromedriver_path)
    driver.get('https://www.pro-football-reference.com/years/1998/index.htm')




    #This is the while loop that our code sits in. It is counting down by year, and we are scraping ~something~ from every winning team

    x=1999


    while (x>1966):
        

        #finding the winning teams page
        teamPage = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[1]/div[2]/p[1]/a')  #Finds winning team element
        
        #This is the if statement that will click the next page IF it finds the element and makes a soup object of the html
        if teamPage:
            teamPage.click()
            time.sleep(3)
            pageSource = driver.page_source
            soup = bs(driver.page_source, 'lxml')
        
        

        try:
            Scrape_Team_Stats(soup,x)
        except AttributeError:
            print("No team stats scraped for "+str(x))
        
        # try:
        #     Scrape_Team_Conversions(soup,x)
        # except AttributeError:
        #     print("No team conversions scraped for "+str(x))



        #find advanced stats page
        # advancedStatsPage=driver.find_element(By.XPATH, '/html/body/div[2]/div[4]/ul/li[4]/a')

        # #Checks if advanced stats page exists, if it does then it clicks it and makes a soup object of the html
        # if advancedStatsPage:
        #     advancedStatsPage.click()
        #     time.sleep(3)
        #     pageSource=driver.page_source
        #     advancedSoup=bs(driver.page_source, 'lxml')
        
        # try:
        #     Scrape_Team_Advanced_Rushing(advancedSoup,x)
        # except AttributeError:
        #     print("No advanced rushing scraped for "+str(x))

        # try:
        #     Scrape_Team_Advanced_Receiving(advancedSoup,x)
        # except AttributeError:
        #     print("No advanced recieving stats scraped for "+str(x))

        #Scrape_Team_Advanced_Defence(advancedSoup,x)

        #this naviagtes back to the teams regular stats page (non advanced)
        #driver.back()
        
        #this navigates back to the season page 
        driver.back()
        

        #this is where things are getting fucked up I think, 
        #the time.sleep is supposed to wait 3 seconds in the hope that the modal prompt either 
        #appears or not
        time.sleep(3)
        

        #Then this is supposed to be trying to find the previous year button
        #and click it. The exception is if there is the modal prompt (pop up ad) then
        #try refreshing the page, then clicking the previous page button. maybe
        #we need to have it wait a few second after refresh idk tho
        try: 
            lastYear=driver.find_element(By.XPATH, "//a[@class='button2 prev']")
            if lastYear:
                lastYear.click()
        except ElementClickInterceptedException:
            driver.refresh()
            time.sleep(3)
            lastYear=driver.find_element(By.XPATH, "//a[@class='button2 prev']")
            if lastYear:
                lastYear.click()
        x=x-1




    driver.quit()

def Scrape_Team_Stats(soup,yearName):
    #finds the team stats table
    teamStats = soup.find('table', id='team_stats')
    

    # extract the data from the table using Pandas
    df = pd.read_html(str(teamStats),header=0)[0] 

    #creates a csv file with the name of the year and then _team_stats
    csvFileName=str(yearName)+'.csv'
    df.to_csv(csvFileName,header=0,index=False)

def Scrape_Team_Conversions(soup,yearName):
    #finds the team conversions table
    teamConversions = soup.find('table', id='team_conversions')
    

    # extract the data from the table using Pandas
    df = pd.read_html(str(teamConversions),header=0)[0] 

    #creates a csv file with the name of the year and then _team_stats
    csvFileName=str(yearName)+'_team_conversions.csv'
    df.to_csv(csvFileName,header=0,index=False)

def Scrape_Team_Advanced_Rushing(soup,yearName):
    #finds the team advanced rushing headers and data in adv rushing table
    teamAdvRushingHeaders = soup.find('table', id='advanced_rushing').find('thead')
    teamAdvRushingData = soup.find('table', id='advanced_rushing').find('tfoot')



    #these 2 for loops are creating lists of the row headers and the actual data
    #then it is deleting the first header row and adding this to a csv file
    headers = []
    for row in teamAdvRushingHeaders.find_all('tr'):
        row_headers = []
        for cell in row.find_all('th'):
            row_headers.append(cell.text.strip())
        headers.append(row_headers)
    #print(headers)
    data = []
    for row in teamAdvRushingData.find_all('tr'):
        row_data = []
        for cell in row.find_all('td'):
            row_data.append(cell.text.strip())
        data.append(row_data)
    
    del headers[0][0]

    # extract the data from the table using Pandas
    df = pd.DataFrame(data,columns=headers)

    csvFileName=str(yearName)+'_team_advanced_rushing_stats.csv'
    df.to_csv(csvFileName,index=False)

def Scrape_Team_Advanced_Receiving(soup,yearName):
    #finds the team stats table
    teamAdvReceivingHeaders= soup.find('table', id='advanced_receiving').find('thead')
    teamAdvReceivingData = soup.find('table', id='advanced_receiving').find('tfoot')


    headers = []
    for row in teamAdvReceivingHeaders.find_all('tr'):
        row_headers = []
        for cell in row.find_all('th'):
            text = cell.text.strip()
            # Replace NaN with empty string
            if text == '':
                text = ' '
            row_headers.append(text)
        headers.append(row_headers)

    #print(headers)

    data = []
    for row in teamAdvReceivingData.find_all('tr'):
        row_data = []
        for cell in row.find_all('td'):
            text = cell.text.strip()
            # Replace NaN with empty string
            if text == '':
                text = ' '
            row_data.append(text)
        data.append(row_data)
    
    del headers[0][0]
    

    # extract the data from the table using Pandas
    df = pd.DataFrame(data,columns=headers)

    csvFileName=str(yearName)+'_team_advanced_recieiving_stats.csv'
    df.to_csv(csvFileName,index=False)



main()