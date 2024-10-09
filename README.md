# 🎶 Hamilton Lyrics Scraper 🎶

Welcome to **Hamilton Lyrics Scraper**! This Python project scrapes and compiles lyrics from the musical *Hamilton* by pulling data from a web source and organizing it into directories. This project uses `requests` and `BeautifulSoup` for scraping and `re` for some regex magic. If you're a fan of *Hamilton* and want the lyrics neatly organized, you're in the right place!

## ✨ Features
- 🚀 **Scrapes** lyrics directly from a web page
- 📁 **Organizes** lyrics into directories by acts (Act 1 & Act 2)
- 📝 Generates a **master lyrics file** containing all the songs

## 🧑‍💻 How It Works
1. Reads song names from a text file.
2. Scrapes song links from the source webpage.
3. Downloads and saves lyrics in separate files for each song, categorized by acts.
4. Compiles all lyrics into a master file.

### 🗂️ Project Structure
```
Hamilton_Lyrics/
│
├── Lyrics/
│   ├── Act1/
│   └── Act2/
│
├── SongNames.txt     # Contains a list of all Hamilton song titles
├── SongLinkPairs.txt # Generated file with song name and link pairs
└── lyrics_scraper.py # Main script to run the scraper
```

## 🚀 Getting Started

### 📦 Prerequisites

Make sure you have the following installed:
- Python 3.x
- `requests` library
- `beautifulsoup4` library

### 🛠️ Installation & Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/hamilton-lyrics-scraper.git
   ```
2. Navigate to the project directory:
   ```bash
   cd hamilton-lyrics-scraper
   ```
3. Create a `SongNames.txt` file in the `Hamilton_Lyrics` folder with the list of Hamilton song names (or use the file provided).

4. Run the scraper:
   ```bash
   python lyrics_scraper.py
   ```

### 🎵 Example `SongNames.txt`:
```txt
Alexander Hamilton
My Shot
The Schuyler Sisters
You'll Be Back
Non-Stop
...
```

## 🛠️ Technologies Used
- **Python**: For the main logic
- **Requests**: For sending HTTP requests to the lyrics page
- **BeautifulSoup**: For parsing HTML content
- **Regex (re)**: For cleaning up song names and links

## 📄 Disclaimer
I do not own these lyrics and this was made as a personal project for my own shenigangs. All rights go to the Hamilton team.

## 👏 Acknowledgements
- Inspired by the amazing **Hamilton** musical by Lin-Manuel Miranda.
- Thanks to **AllMusicals** for providing the song lyrics!
