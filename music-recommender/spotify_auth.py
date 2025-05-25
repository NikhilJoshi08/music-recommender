import spotipy
from spotipy.oauth2 import SpotifyOAuth

CLIENT_ID = 'aae93f805cb54732a5f5b90926e1f330'
CLIENT_SECRET = '484b89a740f64fadb86fef06e0455a8b'
REDIRECT_URI = 'http://127.0.0.1:8888/callback'  # updated loopback IP

# Permissions your app needs
scope = "user-read-recently-played user-library-read"

def authenticate_spotify():
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        redirect_uri=REDIRECT_URI,
        scope=scope,
        cache_path=".cache"
    ))
    return sp

if __name__ == "__main__":
    sp = authenticate_spotify()
    results = sp.current_user_recently_played(limit=5)
    print("Your 5 most recently played tracks:")
    for idx, item in enumerate(results['items']):
        track = item['track']
        print(f"{idx+1}. {track['name']} by {track['artists'][0]['name']}")

#print(results)  # to see raw API response

