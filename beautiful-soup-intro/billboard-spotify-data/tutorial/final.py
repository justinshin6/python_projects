from pprint import pprint

import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyOAuth
from bs4 import BeautifulSoup
import requests
from decouple import config
URL = "https://www.billboard.com/charts/hot-100/"

date = input("Which year do you want to go for billboard hot 100? Type the date in YYYY-MM-DD format: ")

year = date.split("-")[0]
response = requests.get(URL + date)
soup = BeautifulSoup(response.text, 'html.parser')
song_names = soup.find_all(name="h3", id="title-of-a-story", class_="a-no-trucate")
song_list = [song.getText().strip("\n\t") for song in song_names]

CLIENT_ID = config("CLIENT_ID")
CLIENT_SECRET = config("CLIENT_SECRET")
print("I'm now Here")

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt"
    )
)
print("I'm Here")
user_id = sp.current_user()["id"]

song_uris = []

for i in range(len(song_list)):
    result = sp.search(q=f"track:{song_list[i]} year:{year}", type="track")
    print(f"Loading Song {i}:")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        continue
        print(f"{song} doesn't exist in Spotify. Skipped.")

print("Finished! Starting to Make Playlist")
playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
# print(playlist)

sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)

print("Playlist made! ")