import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

URL = 'https://www.billboard.com/charts/hot-100/'
CLIENT_ID = 'YOUR CLIENT ID'
CLIENT_SECRET = 'YOUR CLIENT SECRET'
SPOTIFY_USERNAME = 'YOUR SPOTIFY USERNAME'

date = input('Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ')
response = requests.get(URL + date) 
soup = BeautifulSoup(response.text, 'html.parser')
song_names_spans = soup.select('li ul li h3')
song_names = [span.getText() for span in song_names_spans]

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt",
        username=SPOTIFY_USERNAME, 
    )
)
user_id = sp.current_user()["id"]

song_uris = []
year = date.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    if result["tracks"]["items"]:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
        print(f"Added {song} to the playlist.")
    else:
        print(f"{song} doesn't exist in Spotify. Skipped.")
        
playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)