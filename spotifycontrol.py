import spotipy
from spotipy.oauth2 import SpotifyOAuth

#INFO FOR PUBLIC API, DONT RELEASE TILL MADE PUBLIC ON SPOTIFYS DEV SITE
SPOTIPY_CLIENT_ID='2fa273ca33634531a5f790b92dd5951c'
SPOTIPY_CLIENT_SECRET='83b5b0087bee4e61897598981eac3121'
SPOTIPY_REDIRECT_URI='http://example.com/callback/'

scope = "user-read-playback-state,user-modify-playback-state"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET, SPOTIPY_REDIRECT_URI, scope = scope))

def playspotify(str):
    # check playing devices
    res = sp.devices()
    #print(res)
    search_str = str
    results = sp.search(q=search_str, limit=1)
    if results['tracks']['items']:
        first_track = results['tracks']['items'][0]
        song_uri = first_track['uri']
        print('song uri: '+song_uri)

    # Change track
    sp.start_playback(uris=[song_uri])
