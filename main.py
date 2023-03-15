from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth


# ---- USING SOUP TO SCRAP SONG LIST ----- #

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
response = requests.get("https://www.billboard.com/charts/hot-100/" + date)

soup = BeautifulSoup(response.text, 'html.parser')
songs_names = soup.select(selector="li h3", class_="c-title")

songs_list = [song.getText().strip() for song in songs_names]
print(songs_list)

# ------- Spotify ---------- #

Client_ID = "5b22b2c40d3642c69a616f8ed03d6706"
Client_Secret = "b714d79aa7f246b89f47d763a9bf50c1"
Redirect_Url = "http://example.com"
Cache_path = "token.txt"
Scope = 'playlist-modify-public'

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=Client_ID,
        client_secret=Client_Secret,
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]


# ------- Search Songs  ---------- #

song_uris = []
year = date.split("-")[0]
for song in songs_list:
    # search for songs using name and year
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    # print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")


# create a new playlist
playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
print(playlist)

# Adding songs found into the new playlist
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
