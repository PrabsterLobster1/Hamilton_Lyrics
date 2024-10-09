import requests
from bs4 import BeautifulSoup
import re

def getSongNames(txtFile):
    
    songNamesList = []

    with open(txtFile) as songNames:
        for songName in songNames.readlines():
            songNamesList.append(songName.strip())
    
    return songNamesList

def getSongLinks(songNamesList, mainPagesURL):

    filteredHrefs = []
    response = requests.get(mainPagesURL)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        # Get all links in page
        hrefs = [a['href'] for a in soup.select('body > section.main-layout-content a')]
    
    # Filter song links from links

    for songName in songNamesList:
        cleaned_name = re.sub(r'[?#()\s\'\-,]', '', songName.lower())
        
        for href in hrefs:
            if cleaned_name in href:
                filteredHrefs.append(href)
                hrefs.remove(href)
                break

    return filteredHrefs

def writeSongLinkFile(songNames, hrefs):
    with open("Hamilton_Lyrics\SongLinkPairs.txt","w") as songLinkFile:

        for songName in songNames:
                songLinkFile.write(songName + "^" + hrefs[songNames.index(songName)] +"\n")
    
songNamesList = getSongNames("Hamilton_Lyrics\SongNames.txt")
writeSongLinkFile(songNamesList, getSongLinks(songNamesList, "https://www.allmusicals.com/h/hamilton.htm"))

        