from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from decouple import config

'''
Program that gets a date from the user and creates a Spotify playlist of the top 100 songs according 
to Billboard Music at that specific date. 
'''

# set up Client_ID and Client_Secret using config
CLIENT_ID = config('CLIENT_ID')
CLIENT_SECRET = config('CLIENT_SECRET')
# set up spotify authentication to get spotify token (access code)
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-public",
        redirect_uri="https://example.com",
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        show_dialog=True,
        cache_path="beautiful-soup-intro/billboard-spotify-data/token.txt"
    )
)
# user id
user_id = sp.current_user()["id"]

# check to see if playlist name already in Spotify library 
playlists = sp.user_playlists(user=user_id)['items']
existing_playlist_names = []
for i in range(len(playlists)):
    existing_playlist_names.append(playlists[i]['name'])

# check whether or not the year is a valid year 
valid_year = False
while not valid_year:
    # get the user input date
    user_input_data = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
    curr_year = user_input_data.split('-')[0]
    PLAYLIST_NAME = f'Billboard Top 100 Playlist {user_input_data}'

    if PLAYLIST_NAME not in existing_playlist_names:
        valid_year = True
    else:
        print(f"The playlist name {PLAYLIST_NAME} is already in your library. Try another date.")

# set up variables 
PLAYLIST_DESCRIPTION = f'This is a playlist that contains the top 100 songs on the Billboard top 100 \
    on the date {user_input_data}'
URL = f'https://www.billboard.com/charts/hot-100/{user_input_data}/'
response = requests.get(URL)
billboard_webpage = response.text
soup = BeautifulSoup(billboard_webpage, 'html.parser')

# get the titles from the BillBoard website and get song_uri from the titles
title_tags = soup.find_all(name='h3', id='title-of-a-story', class_='a-no-trucate')
titles = [title.getText().strip() for title in title_tags]
song_uris = []
for title in titles:
    result = sp.search(q=f"track:{title} year:{curr_year}", type="track")
    try:
        uri = result['tracks']['items'][0]['uri']
        song_uris.append(uri)
    except IndexError:
        print(f"{title} not found in Spotify. Skipped")


# if there are available songs to add, then we add a spotify playlist 
if len(song_uris) > 0:

    # create a new spotify playlist
    playlist = sp.user_playlist_create(
        user=user_id,
        name=PLAYLIST_NAME,
        public= True,
        description=PLAYLIST_DESCRIPTION,
    )

    # get the id of the playlist and then add the song_uri's of the current year to the playlist
    playlist_id = playlist['id']

    sp.playlist_add_items(
        playlist_id=playlist_id,
        items=song_uris,
    )
    print(f"Succesfully created {PLAYLIST_NAME} for the date {user_input_data}!!")
else:
    # if there are no songs to add, then that means the year is not valid. 
    print(f"There seems to be no songs for the date {user_input_data}. Try again.")