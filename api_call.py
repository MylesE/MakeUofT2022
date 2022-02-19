import spotipy
from spotipy.oauth2 import SpotifyOAuth

scope = "user-read-playback-state, user-modify-playback-state"

# sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="id",
#                                                client_secret="secret",
#                                                redirect_uri="https://localhost:8080",
#                                                scope=scope))


def doAction(result):
    # currently only supports playing by album but more cases can be added to pause/play
    playbackData = sp.current_playback()
    if result == 'pp':
        togglePlay(playbackData)
    elif result == 'fw':
        fastForward()
    else:
        playAlbum(result)

def playAlbum(uri):
    print("Playing album: " + uri)
    sp.start_playback(context_uri=uri)

def togglePlay(playbackData):
    if playbackData["is_playing"] is True:
            sp.pause_playback()
    else:
            sp.start_playback()

def fastForward():
    sp.next_track()
