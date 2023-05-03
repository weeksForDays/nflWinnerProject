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

def createMasterTeamStatsTable():

    totYardsDfMaster=pd.DataFrame()
    passingDfMaster=pd.DataFrame()
    rushingDfMaster=pd.DataFrame()
    penaltiesDfMaster=pd.DataFrame()
    avgDriveStatsDfMaster=pd.DataFrame()


    x=2000
    while x<=2022:
        totYardsFileName=str(x)+'_total_yards_turnovers_stats.csv'
        totYardsDf = pd.read_csv(totYardsFileName,header=0)
        # add a new index column with the same index value for all rows
        totYardsDf['index'] = (x-2000)

        # set the index column as the index for df_new
        totYardsDf = totYardsDf.set_index('index')
    
        # concatenate df_new with df_master
        totYardsDfMaster = pd.concat([totYardsDf, totYardsDfMaster])
        
        passingFileName=str(x)+'_passing_stats.csv'
        passingDf = pd.read_csv(passingFileName,header=0)

        passingDf['index']= (x-2000)
        passingDf=passingDf.set_index('index')
        passingDfMaster = pd.concat([passingDf,passingDfMaster])


        rushingStatsFileName=str(x)+'_rushing_stats.csv'
        rushingDf = pd.read_csv(rushingStatsFileName,header=0)

        rushingDf['index']= (x-2000)
        rushingDf=rushingDf.set_index('index')
        rushingDfMaster = pd.concat([rushingDf,rushingDfMaster])

        penaltiesStatsFileName=str(x)+'_penalties_stats.csv'
        penaltiesDf = pd.read_csv(penaltiesStatsFileName,header=0)

        penaltiesDf['index']= (x-2000)
        penaltiesDf=penaltiesDf.set_index('index')
        penaltiesDfMaster = pd.concat([penaltiesDf,penaltiesDfMaster])

        avgDriveStatsFileName=str(x)+'_avg_drive_stats.csv'
        avgDriveStatsDf = pd.read_csv(avgDriveStatsFileName,header=0)
        
        avgDriveStatsDf['index']= (x-2000)
        avgDriveStatsDf=avgDriveStatsDf.set_index('index')
        avgDriveStatsDfMaster = pd.concat([avgDriveStatsDf,avgDriveStatsDfMaster])
        x=x+1

    totYardsDfMaster.to_csv("totalYardsMaster.csv",index=True)
    passingDfMaster.to_csv("passingDfMaster.csv",index=True)
    rushingDfMaster.to_csv("rushingMaster.csv",index=True)
    penaltiesDfMaster.to_csv("penaltiesMaster.csv",index=True)
    avgDriveStatsDfMaster.to_csv("avgDriveMaster.csv",index=True)


    


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


def createMasterTeamConversionsTable():

    teamConversionsMasterDf=pd.DataFrame()
    
    x=2000
    while x<=2022:
        fileName=str(x)+'_team_conversions.csv'
        teamConversionsDf = pd.read_csv(fileName,header=0)
        # add a new index column with the same index value for all rows
        teamConversionsDf['index'] = (x-2000)

        # set the index column as the index for df_new
        teamConversionsDf = teamConversionsDf.set_index('index')
    
        # concatenate df_new with df_master
        teamConversionsMasterDf = pd.concat([teamConversionsDf, teamConversionsMasterDf])
        
        
        x=x+1

    teamConversionsMasterDf.to_csv("team_conversions_master.csv",index=True)
    

createMasterTeamConversionsTable()


#addNullVals()

#sortTeamStatsData()


#createMasterTeamStatsTable()