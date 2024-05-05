import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

def setup_spotify_client():
    # Set up Spotify client credentials
    client_id = 'bfd4dd86e7294beba632b058f681bce8'
    client_secret = 'bcd8f89b80f14c34a7f9473c2de5d151'
    client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
    return spotipy.Spotify(client_credentials_manager=client_credentials_manager)
