import spotipy
from spotipy.oauth2 import SpotifyOAuth

scope = "user-read-playback-state, user-modify-playback-state"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="id",
                                               client_secret="secret",
                                               redirect_uri="https://localhost:8080",
                                               scope=scope))

def doAction(result):
    # currently only supports playing by album but more cases can be added to pause/play
    playAlbum(result)

def playAlbum(uri):
    print("Playing album: " + uri)
    sp.start_playback(context_uri=uri)
