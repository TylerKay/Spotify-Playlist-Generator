# Spotify Playlist App

## Created by Tyler Kay

## Programs:

- appDriver.py (main program)

  - (Main Program. appDriver.py will startup the localhost web application.)

- recommendedSpotifyPlaylist.py

  - (Methods that were used in the appDriver program)

- addSpotifySongs.py
  - (Program that add songs to a playlist via command line)

## Installations Required:

- Python 3+
- Spotipy
  - pip install spotipy
- Flask
  - pip install Flask

## Instructions:

### Running Python Script

1. Login to https://developer.spotify.com/dashboard/ and click on create an app to recieve a Client ID and Client Secret. In Edit Settings, set Redirect URIs to http://127.0.0.1:8080/.

2. Create a file named ".env". Inside of it, include set your client_id, client_secret, and redirect_uri.

- SPOTIPY_CLIENT_ID=""
- SPOTIPY_CLIENT_SECRET=""
- SPOTIPY_REDIRECT_URI=""

3. Run python3 appDriver.py. This will start the web application that will run on localhost.

4. In your browser, enter 127.0.0.1:5000 as the url.

5. Fill in the Spotify Username, Playlist Name, Playlist Description, and Number of Songs to Add to Playlist and click "Create a Playlist".

### For Windows (running through .exe)

1. Create a file named ".env". Inside of it, include set your client_id, client_secret, and redirect_uri.

- SPOTIPY_CLIENT_ID=""
- SPOTIPY_CLIENT_SECRET=""
- SPOTIPY_REDIRECT_URI=""

2. Run the appDriver.exe script

3. In your browser, enter 127.0.0.1:5000 as the url.

4. Fill in the Spotify Username, Playlist Name, Playlist Description, and Number of Songs to Add to Playlist and click "Create a Playlist".

#### After that, you're all set! Enjoy!

### Notes:

- To convert python script -> .exe, pip install pyinstaller.
  - Command used: pyinstaller -F --add-data "templates;templates" --add-data "static;static" appDriver.py

Last updated: 8/18/22
