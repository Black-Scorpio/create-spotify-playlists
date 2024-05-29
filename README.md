# Billboard Hot 100 Spotify Playlist Creator

This Python script fetches the top 100 songs from the Billboard Hot 100 chart for a specified year and creates a Spotify playlist with those songs.

## Features

- Fetches top 100 songs and their artists from the Billboard Hot 100 chart for a specified year.
- Creates a Spotify playlist with the fetched songs.
- Adds the songs to the created Spotify playlist.

## Requirements

- Python 3.6+
- `requests`
- `beautifulsoup4`
- `spotipy`
- `python-dotenv`

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/Black-Scorpio/create-spotify-playlists.git
    cd create-spotify-playlists
    ```

2. Create a virtual environment:
    ```sh
    python -m venv venv
    source venv/bin/activate   # On Windows use `venv\Scripts\activate`
    ```

3. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```

4. Create a `.env` file in the project directory and add your Spotify API credentials:
    ```plaintext
    SPOTIPY_CLIENT_ID=your_spotify_client_id
    SPOTIPY_CLIENT_SECRET=your_spotify_client_secret
    SPOTIPY_REDIRECT_URI=http://localhost:3000
    ```

5. Create a `.gitignore` file to exclude sensitive information and unnecessary files:
    ```plaintext
    # Ignore environment variables
    .env

    # Ignore Spotify token cache
    .cache

    # Virtual environment
    venv/
    ```

## Usage

1. Run the script:
    ```sh
    python script.py
    ```

2. Enter the year you want to fetch the Billboard Hot 100 chart for (in the format `YYYY-MM-DD`).

3. The script will create a Spotify playlist with the top 100 songs for the specified date.

