# Import necessary libraries
import requests  # for sending HTTP requests
from bs4 import BeautifulSoup  # for parsing HTML content
import re  # for working with regular expressions

# Function to read song names from a file
# Input: txtFile (string) - Path to a text file that contains the song names
# Output: songNamesList (list of strings) - List of song names
def getSongNames(txtFile):
    
    songNamesList = []  # Initialize an empty list to store song names

    # Open the file and read each line (each song name)
    with open(txtFile) as songNames:
        for songName in songNames.readlines():
            songNamesList.append(songName.strip())  # Strip leading/trailing whitespace and add to the list
    
    return songNamesList  # Return the list of song names

# Function to get song links based on song names
# Input: 
#   - songNamesList (list of strings) - List of cleaned song names
#   - mainPagesURL (string) - URL of the webpage that contains song links
# Output: filteredHrefs (list of strings) - List of filtered song URLs
def getSongLinks(songNamesList, mainPagesURL):

    filteredHrefs = []  # Initialize an empty list to store filtered links
    response = requests.get(mainPagesURL)  # Send a GET request to fetch the page
    if response.status_code == 200:  # Check if the request was successful
        soup = BeautifulSoup(response.content, 'html.parser')  # Parse the HTML page

        # Get all anchor links in the body section of the webpage
        hrefs = [a['href'] for a in soup.select('body > section.main-layout-content a')]
    
    # Filter song links based on the song names
    for songName in songNamesList:
        # Clean the song name by removing specific characters and making it lowercase
        cleaned_name = re.sub(r'[?#()\s\'\-,]', '', songName.lower())
        
        # Find the first matching href that contains the cleaned song name
        for href in hrefs:
            if cleaned_name in href:
                filteredHrefs.append(href)  # Add the filtered link to the list
                hrefs.remove(href)  # Remove the matched link from hrefs to avoid duplicates
                break  # Exit the inner loop once a match is found

    return filteredHrefs  # Return the list of filtered song links

# Function to write the song name-link pairs to a file
# Input:
#   - songNames (list of strings) - List of song names
#   - hrefs (list of strings) - List of corresponding song links
# Output: None (writes data to file)
def writeSongLinkFile(songNames, hrefs):
    # Open the file in write mode and create song name-link pairs
    with open("Hamilton_Lyrics\SongLinkPairs.txt","w") as songLinkFile:
        for songName in songNames:
            # Write each song name with its corresponding URL, separated by '^'
            songLinkFile.write(songName + "^" + hrefs[songNames.index(songName)] + "\n")
    
# Main execution:
# Read the song names from the file and get the corresponding links from the webpage
songNamesList = getSongNames("Hamilton_Lyrics\SongNames.txt")
writeSongLinkFile(songNamesList, getSongLinks(songNamesList, "https://www.allmusicals.com/h/hamilton.htm"))
