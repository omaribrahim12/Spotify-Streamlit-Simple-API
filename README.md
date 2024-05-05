## This Python script utilizes the Streamlit framework to create a simple user interface for interacting with the Spotify API. It allows users to perform the following actions:

    Search for Top Tracks by Artist: Retrieve the top 10 hits by a given artist.

    Search for Track: Search for tracks by name and display information about the tracks found.

    Lyrics: Retrieve lyrics for a given track using the Lyrics.ovh API.

### Prerequisites

Before running the script, ensure you have the following installed:

    Python (3.x recommended)
    Streamlit
    Requests library (pip install requests)
    A Spotify Developer account with API access and client credentials (referenced in spotify_setup.py)

### Installation

    Clone this repository or download the script file (spotify_streamlit.py) to your local machine.

    Install the required Python libraries mentioned in the prerequisites.

    Ensure your Spotify API credentials are set up and stored securely. Modify spotify_setup.py accordingly if needed.

### Usage

    Run the script using Python:

    arduino

    streamlit run spotify_streamlit.py

    Access the Streamlit app in your web browser.

    Use the sidebar to select the desired option:
        Search for Top Tracks by Artist
        Search for Track
        Lyrics

    Follow the prompts and input fields to interact with the Spotify API.

### Notes

    This script provides a basic demonstration of how to interact with the Spotify API using Streamlit. You can extend and customize it according to your requirements.
    Ensure proper error handling and exception management for production use.
    Refer to the official documentation of Streamlit and Spotify API for more information and advanced usage.

### Feel free to adjust the content as needed to provide additional details or instructions!
