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


# add the Firefox incognito mode alternative
options.set_preference("browser.privatebrowsing.autostart", True)

driver = webdriver.Firefox(options=options, executable_path=geckodriver_path)
driver.get('https://www.pro-football-reference.com/years/2022/index.htm')

#soup = bs(driver.page_source, 'lxml')



    


# df=pd.read_html(firstTable)

# df.to_csv('bitch.csv',index=False)




# screen_height = driver.execute_script('return window.screen.height;')
# i = 1.5

# while True:
#     driver.execute_script('window.scrollTo(0, {screen_height}*{i}-4);'.format(screen_height=screen_height-4, i=i))
#     i += 1
#     time.sleep(3)

#     scroll_height = driver.execute_script('return document.body.scrollHeight;')

#     if (((screen_height) * i > scroll_height) or (i > 3)):
#         break



#This is the while loop that our code sits in. It is counting down by year, and we are scraping ~something~ from every winning team


df_dict = {}

x=2022


while (x>2019):
    
    
    
    teamPage = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[1]/div[2]/p[1]/a')  #Finds winning team element
    
    #This is the if statement that will clicks the next page and makes a soup object of the html
    if teamPage:
        teamPage.click()
        pageSource = driver.page_source
        soup = bs(driver.page_source, 'lxml')
    
    # #Finding the header names for the data frames
    # teamStats = soup.find('table', id='team_stats')
    # bothHeaders=teamStats.find('thead').find_all('tr')
    # teamStatsColumnHeaders=bothHeaders[1].find_all('th')

    # totYardsheaders=[]
    # passingHeaders=[]
    # rushingHeaders=[]
    # penaltiesHeaders=[]
    # averageDriveHeaders=[]
    # miscHeaders=[]

    # for columnName in teamStatsColumnHeaders:
    #     if 'data-over-header' in columnName.attrs and columnName['data-over-header'] == 'Tot Yds & TO':
    #         totYardsheaders.append(columnName.get_text(strip=True))

    #     elif 'data-over-header' in columnName.attrs and columnName['data-over-header'] == 'Passing':
    #         passingHeaders.append(columnName.get_text(strip=True))
    #     elif 'data-over-header' in columnName.attrs and columnName['data-over-header'] == 'Rushing':
    #         rushingHeaders.append(columnName.get_text(strip=True))
    #     elif 'data-over-header' in columnName.attrs and columnName['data-over-header'] == 'Penalties':
    #         penaltiesHeaders.append(columnName.get_text(strip=True))
    #     elif 'data-over-header' in columnName.attrs and columnName['data-over-header'] == 'Average Drive':
    #         averageDriveHeaders.append(columnName.get_text(strip=True))
    #     else:
    #         miscHeaders.append(columnName.get_text(strip=True))
    
    #teamName=driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[1]/div[2]/h1/span[2]')
    
    

    # df = pd.DataFrame(columns=totYardsheaders)
    # df1 = pd.DataFrame(columns=passingHeaders)
    # df2 = pd.DataFrame(columns=rushingHeaders)
    # df3 = pd.DataFrame(columns=penaltiesHeaders)
    # df4 = pd.DataFrame(columns=averageDriveHeaders)
    # df5 = pd.DataFrame(columns=miscHeaders)
    



    
    
   
    

    


    # # Add dataframe to dictionary
    # df_dict[f'df_{teamName}_total_yard_and_TO'] = df
    # df_dict[f'df_{teamName}_passing_stats'] = df1
    # df_dict[f'df_{teamName}_rushing_stats'] = df2
    # df_dict[f'df_{teamName}_penalties_stats'] = df3
    # df_dict[f'df_{teamName}_average_drive_stats'] = df4
    # df_dict[f'df_{teamName}_misc_stats'] = df5


    table = soup.find('table', id='team_stats')

    # extract the data from the table using Pandas
    df = pd.read_html(str(table),header=0)[0]  
    csvFileName=str(x)+'.csv'
    df.to_csv(csvFileName,header=0)

    driver.back()
    lastYear=driver.find_element(By.XPATH, "//a[@class='button2 prev']")
    if lastYear:
        lastYear.click()
    x=x-1

    # print("TotYard: ")
    # print(totYardsheaders)
    # print("Passing: ")
    # print(passingHeaders)
    # print("Rushing: ")
    # print(rushingHeaders)
    # print("Penalties: ")
    # print(penaltiesHeaders)
    # print("Average Drive: ")
    # print(averageDriveHeaders)
    # print("misc: ")
    # print(miscHeaders)
    
    












# firstTable = soup.find('table', id='team_stats')

# bothHeaders=firstTable.find('thead').find_all('tr')

# columnHeaders=bothHeaders[1].find_all('th')



# headers=[]

# for columnName in columnHeaders:
#     headers.append(columnName.get_text(strip=True))

# print(headers)
#print(df_dict)


#driver.close()