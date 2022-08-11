Created by Tyler Kay

Programs:
	appDriver.py (main program)
		(Main Program. appDriver.py will startup the localhost web application.)



	recommendedSpotifyPlaylist.py 
		(Methods that were used in the appDriver program)
	
	addSpotifySongs.py
		(Program that add songs to a playlist via command line)
	
Installations Required: 
	-Python	3+
	-Spotipy
		-pip install spotipy
	-Flask
		-pip install Flask

Instructions:
1. Login to https://developer.spotify.com/dashboard/ and click on create an app to recieve a Client ID and Client Secret. In Edit Settings, set Redirect URIs to http://127.0.0.1:8080/.

2. Use the following commands in Powershell(Windows)/Terminal(Mac/Linux) to set the following environmental variables:
	For Windows:
		set SPOTIPY_CLIENT_ID='your-spotify-client-id'
		set SPOTIPY_CLIENT_SECRET='your-spotify-client-secret'
		set SPOTIPY_REDIRECT_URI='your-app-redirect-url'
		
		OR 
		Manually enter it in via control panel.
		In Control Panel, search environmental variable on the top right search bar
		and select "Edit the system environment variables"--> "Environmental Variables". 
		Under System variables, select New and enter the provided Variable name and variable Value 
	
	For Mac/Linux:
		export SPOTIPY_CLIENT_ID='your-spotify-client-id'
		export SPOTIPY_CLIENT_SECRET='your-spotify-client-secret'
		export SPOTIPY_REDIRECT_URI='your-app-redirect-url'

3. Run appDriver.py. This will start the web application that will run on localhost.

4. In your browser, enter 127.0.0.1:5000 as the url.

5. Fill in the Spotify Username, Playlist Name, Playlist Description, and Number of Songs to Add to Playlist and click "Create a Playlist".



After that, you're all set! Enjoy!
			