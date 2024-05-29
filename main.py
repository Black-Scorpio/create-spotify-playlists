from pprint import pprint
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os


def fetch_artist_song_list(year):
    """
    Fetches the top 100 songs and their artists from the Billboard Hot 100 chart for a given year.

    Args:
        year (str): The year in the format YYYY-MM-DD to fetch the Billboard Hot 100 chart.

    Returns:
        list: A list of dictionaries, each containing an artist and their corresponding list of songs.
    """
    url = f"https://www.billboard.com/charts/hot-100/{year}/"
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        songs = soup.select(".chart-results-list li h3")
        artists = soup.select(".chart-results-list li span.c-label")

        songs_list = [song.text.strip() for song in songs]
        artists_list = [artist.text.strip() for artist in artists if not artist.text.strip().isdigit()]

        artist_songs_dict = {}
        for song, artist in zip(songs_list, artists_list):
            if artist in artist_songs_dict:
                artist_songs_dict[artist].append(song)
            else:
                artist_songs_dict[artist] = [song]

        # Converting dictionary to list of dictionaries
        result = [{"artist": artist, "songs": songs} for artist, songs in artist_songs_dict.items()]
        return result

    else:
        print("Failed to retrieve the webpage.")
        return []

def create_spotify_playlist(year, artist_song_list):
    """
    Creates a Spotify playlist for the given year and adds the top songs to it.

    Args:
        year (str): The year for which the playlist is created.
        artist_song_list (list): A list of dictionaries containing artists and their songs.
    """
    print(f"Generating playlist for {year} Billboard 100")
    sp = spotipy.Spotify(
        auth_manager=SpotifyOAuth(
            scope="playlist-modify-private",
            redirect_uri=os.getenv('SPOTIPY_REDIRECT_URI'),
            client_id=os.getenv('SPOTIPY_CLIENT_ID'),
            client_secret=os.getenv('SPOTIPY_CLIENT_SECRET'),
            show_dialog=True,
            cache_path="token.txt"
        )
    )
    user_id = sp.current_user()["id"]

    uris = []

    for item in artist_song_list:
        artist = item["artist"]
        for song in item["songs"]:
            query = f"track: {song} artist: {artist} year: {year[:4]}"
            results = sp.search(query, type='track', limit=20)
            try:
                uri = results['tracks']['items'][0]["uri"]
                uris.append(uri)
            except IndexError:
                print(f"{song} by {artist} does not exist on Spotify")

    playlist = sp.user_playlist_create(user=user_id, name=f"{year} Billboard 100", public=False, description=f"Playlist for {year}")
    sp.playlist_add_items(playlist_id=playlist['id'], items=uris)


if __name__ == "__main__":
    load_dotenv()
    YEAR = input("What year would you like to go back in time to and have a listen for? (YYYY-MM-DD): ")
    artist_song_list = fetch_artist_song_list(YEAR)
    create_spotify_playlist(YEAR, artist_song_list)
