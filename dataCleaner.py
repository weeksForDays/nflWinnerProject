from bs4 import BeautifulSoup as bs
import requests
import pandas as pd
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import json


#Replaces Nan vales with a space
def addNullVals():
    x=2002
    while x<=2022:
        fileName=str(x)+'.csv'
        #Reads in the CSV file
        df = pd.read_csv(fileName,index_col=None)

        #Replaces empty strings with a space
        df = df.replace({'NaN': ' '})

        df.to_csv(fileName,index=False)
        x=x+1


def sortTeamStatsData():
    x=2002
    while x<=2022:
        fileName=str(x)+'.csv'
        #Reads in the CSV file adding a header row
        df = pd.read_csv(fileName,header=0)


        
            
        totYardsheaders=[]
        passingHeaders=[]
        rushingHeaders=[]
        penaltiesHeaders=[]
        averageDriveHeaders=[]
        miscHeaders=[]

        



        



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
        x=x+1