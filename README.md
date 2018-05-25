# General
This project provides a main and a side/bonus functionality.
The main functionality is to enable a user to convert a youtube playlist into a Spotify playlist.

We provide a second service, which enables user to find out if a song is more "male" or "female". We will detail the usage of this extra functionality at the end of this document: (link here)

## Youtube to Spotify playlist
Clone or download this repository.

**Please** Before trying to run our code, follow the below steps.

### Browser

The code uses google Chrome to "scrap" the youtube playlist, hence, you need to have downloaded Chrome.

### imports
The source code is in Python and requires several modules. Please make sure you have:

selenium

tqdm

Requests

bs4

spotify_api

json

### Personal information
In order to access and modify your Spotify account we need you to provide a valid authentification token.

1- Click the following link: [get token](https://beta.developer.spotify.com/console/post-playlists/) 

2- Click on the "GET TOKEN" button

3- Login with your Spotify account

4- Tick the boxes "playlist-modify-public" and "playlist-modify-private"

5- Click on "REQUEST TOKEN"

6- Copy the entire content of the "OAuth Token" field (double click in it)

7- Open the api_key.py file and paste the content in the SPOTIFY_TOKEN variable, within the "".

8- Save the api_key.py file 

**Note: The authentification Token is valid for approx. 15 minutes, so you might be asked to repeat this operation again if your token has expired**

### Running the Code

Now (if you have successfully completed the previous parts) the fun begins. In your command line navigate into the repository you just cloned or downloaded, and type "Python youtube_playlist.py"

You will be asked to provide information:

1- You will be asked to provide the link to the youtube playlist: mind you need to provide link to the "playlist homepage" (URL must start with "https://www.youtube.com/playlist): like the following [example](https://www.youtube.com/playlist?list=PLDzVECoc2lpTFnCQTzTK8RIRnuFW-fFbu)

2- You will then be asked to provide your Spotify username, provide the username of the account you used to retrieve your authentification Token

3- Provide the name of the playlist you wish to create on your Spotify account

4- Provide the description of the playlist you want to create (optional) 

You will see that a Browser page will open, do not touch it, it will be closed when we have retrieved all the necessary information. You will also see a progress bar regarding the "scrapping" of the youtube playlist. Remember, that your authentification Token needs to be valid during the entire process. 
