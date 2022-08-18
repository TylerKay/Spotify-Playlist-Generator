from flask import Flask, redirect, url_for, render_template, request
from recommendedSpotifyPlaylist import *
import math

app = Flask(__name__)

@app.route("/", methods = ["POST", "GET"])
def home():
    if request.method == "POST":
        u_name = request.form["username"]
        p_name = request.form["playlistName"]
        p_description = request.form["playlistDescription"]
        num_songs = request.form["numSongsToAdd"]
        numSongs = int(num_songs)
        if authenticate(u_name) == True:
            createAPlaylist(u_name, p_name, p_description, numSongs)
            
        return (redirect(url_for("success")))
    else:
        return render_template("index.html")


@app.route("/success")
def success():
    return render_template("success.html")


if __name__ == "__main__":
    app.run(debug = False) 
    # When debugging set debug = True

