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
    x=2000
    while x<=2022:
        fileName=str(x)+'_team_advanced_recieving_stats.csv'
        #Reads in the CSV file
        df = pd.read_csv(fileName,index_col=None)

        #Replaces empty strings with a space
        df = df.fillna(' ')
        print("replaced")

        df.to_csv(fileName,index=False)
        x=x+1


def sortTeamStatsData():
    x=2000
    while x<=2001:
        fileName=str(x)+'_team_stats.csv'
        #Reads in the CSV file adding a header row
        df = pd.read_csv(fileName,header=0)
            
        #making a total stats and turnovers data frame    
        totalYardsAndTurnovers = df.iloc[:, [0, 1, 2, 3, 4, 5, 6, 7]]  
        
        #making a passing stats dataframe
        passingStats = df.iloc[:,[0,8,9,10,11,12,13,14]]

        #making a rushing stats dataframe
        rushingStats = df.iloc[:,[0,15,16,17,18,19]]

        #making a penalties stats dataframe
        penalties = df.iloc[:,[0,20,21,22]]

        #making a avg drive stats dataframe
        avgDriveStats = df.iloc[:,[0,23,24,25,26,27,28,29,30]]

        #printing to csv file
        totYardsFileName=str(x)+'_total_yards_turnovers_stats.csv'
        totalYardsAndTurnovers.to_csv(totYardsFileName,index=False)

        passingFileName=str(x)+'_passing_stats.csv'
        passingStats.to_csv(passingFileName,index=False)

        rushingStatsFileName=str(x)+'_rushing_stats.csv'
        rushingStats.to_csv(rushingStatsFileName,index=False)

        penaltiesStatsFileName=str(x)+'_penalties_stats.csv'
        penalties.to_csv(penaltiesStatsFileName,index=False)

        avgDriveStatsFileName=str(x)+'_avg_drive_stats.csv'
        avgDriveStats.to_csv(avgDriveStatsFileName,index=False)






        



        x=x+1



#addNullVals()

sortTeamStatsData()