# General
This project provides a main and a side/bonus functionality.
The main functionality enables a user to convert a youtube playlist into a Spotify playlist.

We provide a second service, which enables user to find out if a song is more "male" or "female". We will detail the usage of this extra functionality at the end of this document: (link here)

## Youtube to Spotify playlist
Clone or download this repository.

**Please** Before trying to run our code, follow the below steps.

### Browser

The code uses google Chrome to "scrap" the youtube playlist, hence, you need to have downloaded Chrome.

### imports
The source code is in Python and requires several modules. Please make sure you have installed the following:
```
selenium

tqdm

requests

bs4

json
```
### Personal information

You will be asked to provide information to enable the service to access your Spotify account.

Spotify username : 
- if you create an account from scratch, provide the	profile name visible when you login to your account.

- if you created an account via facebook logins, you need to provide a different one: login to your spotify account -> go to your profile page -> right click on your name -> share -> copy profile link-> the information is the digit sequence after /user/: ex: https://open.spotify.com/user/**2456320529**?si=yJ0bsbmpQdqEtO-q61d-BA

Spotify Authentification Token:
In order to access and modify your Spotify account we need you to provide a valid authentification token.

1. Click the following link: [get token](https://beta.developer.spotify.com/console/post-playlists/) 

2. Click on the "GET TOKEN" button

3. Login with your Spotify account

4. Tick the boxes "playlist-modify-public" and "playlist-modify-private"

5. Click on "REQUEST TOKEN"

6. Copy the entire content of the "OAuth Token" field (double click in it)

**Note: The authentification Token is valid for approx. 15 minutes, so you might be asked to repeat this operation again if your token has expired**

### Running the Code

Now (if you have successfully completed the previous parts) the fun begins. In your command line navigate into the repository you just cloned or downloaded, and type "Python youtube_playlist.py"

1. You will be asked to provide the link to the youtube playlist: mind you need to provide link to the "playlist homepage" (URL must start with "https://www.youtube.com/playlist): like the following [example](https://www.youtube.com/playlist?list=PLDzVECoc2lpTFnCQTzTK8RIRnuFW-fFbu).
You will see that a Browser page will open, do not touch it, it will be closed when we have retrieved all the necessary information. You will also see a progress bar regarding the "scrapping" of the youtube playlist. 

2. You will then be asked to provide your Spotify username, provide the username of the account you used to retrieve your authentification Token

3. Provide the name of the playlist you wish to create on your Spotify account




4. Provide the description of the playlist you want to create (optional) 

**Once these operations are terminated, you will be notified of the songs that could not be found in the Spotify library. The songs that were found on Spotify are now part of the newly created playlist.**


### Song "Gender" Identification

### Imports

The source code is in Python and requires several modules. Please make sure you have installed the following:
```
requests

json

api_key

BeautifulSoup

Counter

### Running the code

1. You will need to input the item you are searching for

2. You will be asked to input the type of item you are searching for (album/artist/playlist/track)

3. You will need to provide your spotify authentification token as explained here

4. You will be given a list with artists to choose from

5. Accordning to the lyrics the programm will find out if the song is "male" or "female"


