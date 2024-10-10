# Import necessary libraries
import requests  # for sending HTTP requests
from bs4 import BeautifulSoup  # for parsing HTML content
import os  # for interacting with the operating system (e.g., creating directories)
import re  # for working with regular expressions

# Function to get the lyrics from a song's URL
# Input: URL of the song's lyrics page (lyricURL: string)
# Output: A list of filtered and cleaned lyrics (list of strings)
def getSongLyrics(lyricURL):

    filteredLyrics = []  # List to store the processed lyrics line by line
    response = requests.get(lyricURL)  # Send a GET request to fetch the HTML page
    soup = BeautifulSoup(response.content, 'html.parser')  # Parse the HTML page using BeautifulSoup

    # Extract the lyrics from the div with id 'page'
    lyrics_div = soup.find('div', id='page')

    # Get the text from the div and split it into individual lines
    lyrics = lyrics_div.get_text().splitlines()

    # Loop through each line of the lyrics
    for lyric in lyrics:

        # Skip lines that start with "Last Update:" (these are not part of the lyrics)
        if lyric.startswith("Last Update:"):
            continue

        # Add the line to the filtered lyrics list, with any leading spaces removed
        filteredLyrics.append(lyric.lstrip()+"\n")

    return filteredLyrics  # Return the processed lyrics


# Function to initialize song directories and save lyrics into files
# Input: Path to a text file containing song names and their corresponding URLs (txtFile: string)
# Output: None (creates files in the directory with lyrics and a master file containing all lyrics)
def intializeSongDirectories(txtFile):
    
    songNames = []  # List to store the names of the songs
    songLinks = []  # List to store the URLs of the songs

    actName = "Act1"  # Start with Act 1

    # Open the file that contains song names and URLs
    with open(txtFile) as songLinkPairs:
        # Read each line from the file
        for line in songLinkPairs.readlines():
            parsedLine = line.split("^")  # Split each line using '^' to separate song name and URL
            songNames.append(parsedLine[0])  # Append the song name to songNames
            songLinks.append(parsedLine[1])  # Append the song URL to songLinks
    
    # Create and open a master file to store all lyrics
    masterFile = open("Hamilton_Lyrics\Lyrics\MasterLyrics.txt", "w")

    # Loop through each song
    for songName in songNames:
        # Clean the song name by removing certain characters and making it lowercase
        cleaned_name = re.sub(r'[?#()\s\'\-,]', '', songName.lower())

        # Create a file for each song in its respective Act directory
        with open("Hamilton_Lyrics\Lyrics\\" + actName + "\\" + cleaned_name, "w") as songFile:
            # Fetch and write the song lyrics to the file
            for lyric in getSongLyrics(songLinks[songNames.index(songName)]):
                songFile.write(lyric)  # Write the lyric to the song's file
                masterFile.write(lyric)  # Also write the lyric to the master file

            # Switch to Act 2 after the song "Non-Stop"
            if songName == "Non-Stop":
                actName = "Act2"
    
    masterFile.close()  # Close the master file


# Create directories for storing the lyrics if they don't already exist
try:
    os.mkdir("Hamilton_Lyrics\Lyrics")
    os.mkdir("Hamilton_Lyrics\Lyrics\Act1")
    os.mkdir("Hamilton_Lyrics\Lyrics\Act2")

except FileExistsError:  # Ignore the error if the directories already exist
    pass

# Initialize the song directories by reading the song names and URLs from the specified file
intializeSongDirectories("Hamilton_Lyrics\SongLinkPairs.txt")
