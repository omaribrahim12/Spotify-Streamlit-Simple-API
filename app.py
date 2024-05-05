import streamlit as st
import requests
from spotify_setup import setup_spotify_client

# Set up Spotify client
sp = setup_spotify_client()
# Now you can use 'sp' to interact with the Spotify API in your Streamlit app

# Streamlit app
def get_top_tracks_by_artist(artist_name):
    """
    Retrieve the top 10 hits by a given artist.
    """
    results = sp.search(q=artist_name, limit=1, type='artist')
    if results['artists']['items']:
        artist = results['artists']['items'][0]
        artist_id = artist['id']
        
        # Get the artist's top tracks
        top_tracks = sp.artist_top_tracks(artist_id, country='US')
        
        return top_tracks['tracks'][:10]
    else:
        return None
def get_artist_recommendations(artist_name):



    """
    Retrieve related artists as recommendations.
    """
    recommendations = []
    results = sp.search(q=artist_name, limit=10, type='artist')
    if results['artists']['items']:
        for artist in results['artists']['items']:
            recommendations.append(artist['name'])
    return recommendations
def get_lyrics(artist_name, track_name):
    """
    Retrieve lyrics for a given track.
    """
    url = f"https://api.lyrics.ovh/v1/{artist_name}/{track_name}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()['lyrics']
    else:
        return "Lyrics not found."
def search_track(track_name):
    """
    Search for tracks by name.
    """
    results = sp.search(q=track_name, limit=10, type='track')
    if results['tracks']['items']:
        # Sort the tracks by popularity
        sorted_tracks = sorted(results['tracks']['items'], key=lambda x: x['popularity'], reverse=True)
        return sorted_tracks
    else:
        return None

# Streamlit app
st.title('Welcome to my simple Spotify API')
# Image
InterfaceImage = st.image("Home.png")
# Menu to select function
selected_option = st.sidebar.radio("Select Option", ("Search for Top Tracks by Artist", "Search for Track", "Lyrics"))

if selected_option == "Search for Top Tracks by Artist":
    # Search for top tracks by artist
    artist_name = st.text_input('Enter an artist name:')
    if artist_name:
        recommendations = get_artist_recommendations(artist_name)
        selected_recommendation = st.selectbox('Select an artist recommendation:', options=recommendations)
        if selected_recommendation:
            st.write(f"You selected: {selected_recommendation}")
            artist_name = selected_recommendation  # Apply selected artist name
        st.markdown("---")
    
        top_tracks = get_top_tracks_by_artist(artist_name)
    
        
        if top_tracks:
            st.write(f"### Top 10 Hits by {artist_name}:")
            for idx, track in enumerate(top_tracks):
                st.write(f"{idx+1}. [{track['name']}]({track['external_urls']['spotify']}) - {', '.join([artist['name'] for artist in track['artists']])}")
        else:
            st.write("No top tracks found for this artist.")
elif selected_option == "Search for Track":
    # Search for a track
    search_term = st.text_input('Enter a track name:')
    if search_term:
        tracks = search_track(search_term)
        if tracks:
            st.write(f"### Found {len(tracks)} tracks with the name '{search_term}':")
            for idx, track in enumerate(tracks):
                st.write(f"**Track {idx + 1}:**")
                st.write(f"**Name:** [{track['name']}]({track['external_urls']['spotify']})")
                st.write(f"**Artist:** {', '.join([artist['name'] for artist in track['artists']])}")
                st.write(f"**Album:** {track['album']['name']}")
                st.image(track['album']['images'][0]['url'], caption='Album Art', use_column_width=True)
        else:
            st.write("No tracks found.")
elif selected_option == "Lyrics":
    # Search for lyrics
    artist_name = st.text_input('Enter the artist name:')
    track_name = st.text_input('Enter the track name:')
    if artist_name or track_name:
        lyrics = get_lyrics(artist_name, track_name)
        if lyrics:
            st.write('### Lyrics:')
            st.write(lyrics)
        else:
            st.write("Lyrics not found.")
