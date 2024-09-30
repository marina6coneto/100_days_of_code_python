# Day 46: Billboard Hot 100 Playlist Creator

- This project allows you to create a Spotify playlist from the Billboard Hot 100 chart for a specific date.
- Using web scraping and the Spotify API, it fetches song names from the Billboard website and adds them to a private Spotify playlist.

![my playlist](.\screenshot\playlist.png)

## Features

- Scrapes the Billboard Hot 100 songs for a specific date.
- Searches for the songs on Spotify.
- Creates a private Spotify playlist with the found songs.
- Adds songs to the playlist, skipping any songs not found on Spotify.

## Requirements

- Python 3.x
- Spotify Developer Account with Client ID and Client Secret
- Billboard URL access
- `spotipy` library for Spotify API integration
- `BeautifulSoup` and `requests` for web scraping

## Installation

1. Clone this repository:
    ```bash
    git clone https://github.com/yourusername/billboard-playlist-creator.git
    cd billboard-playlist-creator
    ```

2. Install the required Python packages:
    ```bash
    pip install spotipy beautifulsoup4 requests
    ```

3. Set up your Spotify Developer credentials:
    - Go to [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/login).
    - Create an app to get your `Client ID` and `Client Secret`.
    - Add the redirect URI as `http://example.com` in your Spotify App settings.

4. Update the `CLIENT_ID`, `CLIENT_SECRET`, and `SPOTIFY_USERNAME` in the Python script.

## How to Run

1. Run the Python script:
    ```bash
    python main.py
    ```

2. Enter the date in the format `YYYY-MM-DD` when prompted to select the Billboard Hot 100 list for that date.

3. The script will search for the songs on Spotify and add them to a new private playlist in your account.

## Example Usage

```bash
Which year do you want to travel to? Type the date in this format YYYY-MM-DD: 2020-08-01
Added Song1 to the playlist.
Added Song2 to the playlist.
Song3 doesn't exist in Spotify. Skipped.
```