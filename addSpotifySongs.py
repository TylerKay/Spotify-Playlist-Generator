# Created by Tyler Kay

import spotipy
from spotipy.oauth2 import SpotifyOAuth
import json
import random

scope = "playlist-modify-public user-top-read"
username = ""

token = SpotifyOAuth(username=username, scope=scope)
spotifyObject = spotipy.Spotify(auth_manager = token)



print("Let's create a playlist based on the name of the song you provide... ")
# print(spotifyObject.current_user_recently_played(limit = 2, after = None, before = None))
playlistName = input("What's the name of the playlist? ")
playlistDescription = input("What's the description of the playlist? ")


spotifyObject.user_playlist_create(user = username, name = playlistName, public = True, collaborative = False, description = playlistDescription)

songInput = input("Enter the name of song to add to the playlist or type 'quit' to exit: ")
songList = []


while songInput != "quit":
    result = spotifyObject.search(q = songInput)
    # print(json.dumps(result,sort_keys = 4, indent = 4))
    songList.append(result["tracks"]["items"][0]["uri"]) #uri - identification of the song
    songInput = input("Enter another name of a song you would like to add to the playlist or type 'quit': ")

allUserPlaylist = spotifyObject.user_playlists(user = username)
playlistID = allUserPlaylist["items"][0]["id"]

spotifyObject.user_playlist_add_tracks(user = username, playlist_id = playlistID, tracks = songList)

print("Sucessfully added the songs to the playlist. Enjoy! ")