from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36 Edg/140.0.0.0"}
url = f"https://www.billboard.com/charts/hot-100/{date}/"
response = requests.get(url=url, headers=header)
billboard_webpage = response.text
soup = BeautifulSoup(billboard_webpage,"html.parser")
titles = soup.select("li ul li h3")
songs = [song.getText().strip() for song in titles]
print(songs)
client_id = "9b18086414344a24b6fc7670446ba5cc"
client_secret = "f81348b10f95486eabe95ff7876c455e"


sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://127.0.0.1:8000/callback",
        client_id=client_id,
        client_secret=client_secret,
        show_dialog=True,
        cache_path="token.txt",
    )
)
user_id = sp.current_user()["id"]
user_id = "31i6q7khd57uykl6csmkkoi6pjoe"

song_uris = []
year = date.split("-")[0]

for song in songs:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

my_playlist = sp.user_playlist_create(user=user_id,name=f"{date} Billboard 100", public=False)
sp.playlist_add_items(playlist_id=my_playlist["id"],items=song_uris)