# Created by Tyler Kay

import spotipy
from spotipy.oauth2 import SpotifyOAuth
import json
import random
import os
from dotenv import load_dotenv, find_dotenv

scope = "playlist-modify-public user-top-read"

# ---- Go to your Spotify Account Overview and enter in your username. It should be a string of characters or numbers such as "12345678910" or "abcdefghijk"
username = ""

load_dotenv(find_dotenv())

SPOTIPY_CLIENT_ID = os.getenv("SPOTIPY_CLIENT_ID")
SPOTIPY_CLIENT_SECRET = os.getenv("SPOTIPY_CLIENT_SECRET")
SPOTIPY_REDIRECT_URI = os.getenv("SPOTIPY_REDIRECT_URI")

token = SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID, username=username, scope=scope)
spotifyObject = spotipy.Spotify(auth_manager = token)

def getTrackIDs(time_frame):
    trackIDs = []
    for song in time_frame["items"]:
        trackIDs.append(song["id"])
    return trackIDs

def getArtistIDs(time_frame):
    artistIDs = []

    for song in time_frame["items"]:
        artistID = time_frame["items"][0]["artists"][0]["id"]
        artistIDs.append(artistID)

    return artistIDs

def getTopGenres(topArtistIDs):
    topGenresList = []
    for i in range(len(topArtistIDs)):
        curr_artist = spotifyObject.artist(topArtistIDs[i])
        # print(json.dumps(curr_artist,sort_keys = 4, indent = 4))
        curr_artist_genre = spotifyObject.artist(topArtistIDs[i])["genres"] # locate the genres of the current artist 
        
        for genre in curr_artist_genre: # add current artist genres to the topGenreList
            topGenresList.append(genre)
        
        return topGenresList

def getRandomThreeGenreSeeds(genreList):
    newGenreList = []
    for i in range(3):
        rng = random.randrange(len(genreList)-1)
        newGenreList.append(genreList[rng])
    return newGenreList

def authenticate(username):
    scope = "playlist-modify-public user-top-read"
    token = SpotifyOAuth(username=username, scope=scope)
    spotifyObject = spotipy.Spotify(auth_manager = token)
    
    return True

def createAPlaylist(username, playlistName, playlistDescription, numSongs):
    spotifyObject.user_playlist_create(user = username, name = playlistName, public = True, collaborative = False, description = playlistDescription)
    allUserPlaylist = spotifyObject.user_playlists(user = username)
    playlistID = allUserPlaylist["items"][0]["id"]

    topTrackResultsShort = spotifyObject.current_user_top_tracks(limit = 1, time_range = "short_term") # short_term = last 4 weeks, medium_term = last 6 weeks, long_term = calculated by several years of data

    topTrackIDs = getTrackIDs(topTrackResultsShort)

    topArtistIDs = getArtistIDs(topTrackResultsShort)

    topGenres = getTopGenres(topArtistIDs)

    if len(topGenres) > 3: # number of topGenres cannot exceed 3, so we need to limit it by using RNG
        topGenres = getRandomThreeGenreSeeds(topGenres)

    # Getting the recommended songs to a list
    songList = []
    for i in range(numSongs):
        recommendedSongs = spotifyObject.recommendations(seed_artists = topArtistIDs, seed_genres = topGenres, seed_tracks = topTrackIDs, limit = 20)

        songList.append(recommendedSongs["tracks"][0]["uri"])
        # print("Song List: ", songList)


    # Add the songs to the playlist
    spotifyObject.user_playlist_add_tracks(user = username, playlist_id = playlistID, tracks = songList)
