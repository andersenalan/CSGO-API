# Author: John Parkhurst
# Brief: Selenium Web Scraping application for hltv.org

from bs4 import BeautifulSoup
import requests
from config import *
from hltvMatch import *

"""
We are gonna need an iterate method once we properly process all the text on one page, size is done though!
"""


class HltvScraper():
    """
        resultData = login_form = self.driver.find_elements(by=By.CLASS_NAME,value="result-con")

        for element in resultData:
            temp = element.find_element(by=By.XPATH,value=".//a[@class='a-reset']")
            """

    idList =[]
    urlList =[]
    #dictionary
    matchStat = {}

    def gatherSize(self) -> None:
        """
        @brief: We use our field self.page to analyze the page to figure out how many matches there are to scrape!\n
        Sets self.size\n
        :return: None
        """
        soup = BeautifulSoup(self.page.content, "html.parser")
        job_elements = soup.find_all("span", class_="pagination-data")
        # CLEAN THIS UP SLOPPY
        for job_element in job_elements:
            data = job_element.text.split(" ")
            break
        tempMax = 0
        for value in data:
            if value.isnumeric():
                if int(value) > tempMax:
                    tempMax = int(value)
        self.size = tempMax
        return


    def gatherIDURL(self)->None:

        return

    # Looking for class result-con
    def processData(self) -> None:
        """
        @brief: Processes the html we scraped off the page!
        :return: None
        """
        # Result Text
        soup = BeautifulSoup(self.page.content, "html.parser")
        results = soup.find(id="pagination-data")

        # job_elements = soup.find_all("div", class_="result-con")
        # This handles match url and where we get ID
        for link in soup.find_all("a", class_="a-reset"):
            if ('matches' in link.get('href')):
                #print(link.get('href'))
                tempList=link.get('href').split('/')
                self.idList.append(tempList[2])
                self.urlList.append(baseurl+link.get('href'))

        # This Gets all the match data-For each result-con it iterates
        iter=0
        for matchDiv in soup.find_all("div", class_="result-con"):
            # we want class event-name, map-text, div team and div team-won for team names
            # span score-lost,span  score-won
            #Error Coccuring here only registering first match
            #print(matchDiv)
            iter+=1
            break
        print(iter)
        iter=0
        for scoreL, scoreW in zip(soup.find_all("span", class_="score-lost"), soup.find_all("span", class_="score-won")):
            #print(scoreL.text)
            #print(scoreW.text)
            iter+=1
        print(iter)

        iter = 0
        for teamL, teamW in zip(soup.find_all("div", class_="team"),soup.find_all("div", class_="team team-won")):
            print("Won: "+teamW.text)
            #LOST IS WRONG prints both teamW and teamL (check my len of teamL
            print("Lost: "+teamL.text)
            print("NEW MATCH")
            iter+=1
        print(iter)
        if (results != None):
            # print(results.prettify())
            print(self.page.text)
        return

    def report(self):
        """
        @brief a test function where we print out all the data we collect
        :return:
        """
        print("Number of matches:{}".format(self.size))
        print("ID REPORT:")
        for elem in self.idList:
            print("ID IS :{}".format(elem))
        print("URL REPORT:")
        for elem in self.urlList:
            print("URL IS:{}".format(elem))
        return


    # Plan is to iterate through all the matches on said page and put into json of info to add to our api!
    def __init__(self):
        print("Scrape Initiated")
        self.page = requests.get(resulturl)
        self.size = 0
        self.processData()
        try:
            self.gatherSize()
            print("BEEP")
        except:
            print("ERROR")
            return
        #self.report()
        print("DONE")
