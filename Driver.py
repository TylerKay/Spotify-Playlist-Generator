from recommendedSpotifyPlaylist import *

# Enter your username here
username = ""

# Enter the playlist name here
playlistName = ""

# Enter the playlist description here
playlistDescription = ""

# Enter the number of songs you wish to add to your playlist here
numSongs = 5

if authenticate(username) == True:
            try:
                createAPlaylist(username, playlistName, playlistDescription, numSongs)
                print("Success!")
            except:
                print("Something went wrong. Try again")