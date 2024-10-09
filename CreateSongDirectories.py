import requests
from bs4 import BeautifulSoup
import os
import re

def getSongLyrics(lyricURL):

    filteredLyrics = []
    response = requests.get(lyricURL)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract the lyrics
    lyrics_div = soup.find('div', id='page')

    lyrics = lyrics_div.get_text().splitlines()

    for lyric in lyrics:

        if lyric.startswith("Last Update:"):
            continue

        filteredLyrics.append(lyric.lstrip()+"\n")

    return filteredLyrics

        

def intializeSongDirectories(txtFile):
    
    songNames = []
    songLinks = []

    actName = "Act1"

    with open(txtFile) as songLinkPairs:
        for line in songLinkPairs.readlines():
            parsedLine = line.split("^")
            songNames.append(parsedLine[0])
            songLinks.append(parsedLine[1])
    
    # Master File variable creation
    masterFile = open("Hamilton_Lyrics\Lyrics\MasterLyrics.txt", "w")

    for songName in songNames:
        cleaned_name = re.sub(r'[?#()\s\'\-,]', '', songName.lower())

        with open("Hamilton_Lyrics\Lyrics\\" + actName + "\\" + cleaned_name, "w") as songFile:
            for lyric in getSongLyrics(songLinks[songNames.index(songName)]):
                songFile.write(lyric)
                masterFile.write(lyric)


            if songName == "Non-Stop":
                actName = "Act2"
    masterFile.close()


try:
    os.mkdir("Hamilton_Lyrics\Lyrics")
    os.mkdir("Hamilton_Lyrics\Lyrics\Act1")
    os.mkdir("Hamilton_Lyrics\Lyrics\Act2")

except FileExistsError:
    pass

intializeSongDirectories("Hamilton_Lyrics\SongLinkPairs.txt")