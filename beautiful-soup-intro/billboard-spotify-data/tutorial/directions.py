# Step 1: Scraping the Billboard Hot 100

"""
1.) Create a new project in PyCharm and create the main.py file
2.) Create an input() prompt that asks what year you would like to travel to in YYYY-MM-DD format
3.) Scrape the top 100 song titles on that date into a Python list
"""
"""
from bs4 import BeautifulSoup
import requests

URL = "https://www.billboard.com/charts/hot-100/"

date = input("Which year do you want to go for billboard hot 100? Type the date in YYYY-MM-DD format: ")

response = requests.get(URL + date)
soup = BeautifulSoup(response.text, 'html.parser')
song_names = soup.find_all(name="h3", id="title-of-a-story", class_="a-no-trucate")
song_list = [song.getText().strip("\n\t") for song in song_names]
print(song_list)
"""

# Step 2: Authentication with Spotify
"""
1.) You must have an account with Spotify. If you don't already have an account, you can sign up for a free one here
http://spotify.com/signup/
2.) Once you've signed up/signed in, go to the developer dashboard and create a new Spotify App: https://developer.spotify.com/dashboard/
3.) Once you've created a Spotify app, copy the Client ID and Client Secret into your Python Project 
4.) Using the Spotipy documentation, figure out how to authenticate your Python project with Spotify using your unique Client ID/ Client Secret:
https://spotipy.readthedocs.io/en/2.21.0/
5.) Use http://example.com as your Redirect URI. You're looking to get the currentuser id (your Spotify username). 
As per the documentation, make sure you set the redirect URI in the Spotify Dashboard as well.
6.) After successfully authenticating, enter the URL that you found into the prompt in PyCharm 
7.) Then, you should see a token.txt pop up inside of the directory that you are currently in. 
"""
"""
import spotipy
from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=YOUR UNIQUE CLIENT ID,
        client_secret=YOUR UNIQUE CLIENT SECRET,
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]
"""

# Step 3: Step 3 - Search Spotify for the Songs from Step 1
"""
1.) Using the Spotipy documentation, create a list of Spotify song URIs for the list of song names you found from step 1 (scraping billboard 100).
"""
# Step 4: Step 4 - Creating and Adding to Spotify Playlist
"""
1.) Use Spotipy's documentation to create a new private playlist 
2.) Add each of the songs found in Step 3 to the new playlist.

"""

