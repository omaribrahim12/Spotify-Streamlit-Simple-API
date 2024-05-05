import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

def setup_spotify_client():
    # Set up Spotify client credentials
    client_id = 'ENTER_YOUR_CLIENT_ID'
    client_secret = 'ENTER_YOUR_CLIENT_SECRET'
    client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
    return spotipy.Spotify(client_credentials_manager=client_credentials_manager)
