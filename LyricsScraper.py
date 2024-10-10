# Import necessary libraries
import os

# Import the functions from the provided code
from CreateSongLinkFile import getSongNames, getSongLinks, writeSongLinkFile
from CreateSongDirectories import intializeSongDirectories

def main():
    # Step 1: Get song names from the file
    song_names_file = "Hamilton_Lyrics/SongNames.txt"
    song_names_list = getSongNames(song_names_file)
    
    # Step 2: Get song links from the main webpage
    main_page_url = "https://www.allmusicals.com/h/hamilton.htm"
    song_links = getSongLinks(song_names_list, main_page_url)
    
    # Step 3: Write song name-link pairs to a file
    output_link_file = "Hamilton_Lyrics/SongLinkPairs.txt"
    writeSongLinkFile(song_names_list, song_links)
    
    # Step 4: Initialize directories and save lyrics
    intializeSongDirectories(output_link_file)

if __name__ == "__main__":
    main()
