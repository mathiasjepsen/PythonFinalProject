import requests
import json
import api_key


def create_playlist(user_ID, playlist_Name, playlist_Description, spotify_Token):
    global user_id 
    global playlist_name
    global playlist_description
    global spotify_token
    user_id = user_ID
    playlist_name = playlist_Name
    playlist_description = playlist_Description
    spotify_token = spotify_Token
    url_create_playlist = f"https://api.spotify.com/v1/users/{user_id}/playlists"
    headers = {"Accept": "application/json",
               "Content-Type": "application/json",
               "Authorization": f"Bearer {spotify_token}"}
    body = {
        "name": playlist_name,
        "description": playlist_description
    }
    r = requests.post(url_create_playlist, headers=headers, 
                                           data=json.dumps(body))
    results = r.json()
    return results["id"] 



def add_to_playlist(uris, playlist_id):
    url = f"https://api.spotify.com/v1/users/{user_id}/playlists/{playlist_id}/tracks"
    headers = {"Accept": "application/json",
               "Content-Type": "application/json",
               "Authorization": f"Bearer {api_key.SPOTIFY_TOKEN}"}
    body = {
        "uris": uris
    }
    requests.post(url, headers=headers,
                       data=json.dumps(body))


def readFromConsole():
    input_name = input("Hello Sir, may I ask for your username please:")
    input_playlistname = input("Now I will ask you for the name you want to provide for the playlist:")
    input_description = input("Description of the playlist:")
    input_token = input("Your token:")
    print("values you've entered:" + input_name + input_playlistname + input_description, input_token)
    create_playlist(input_name, input_playlistname, input_description, input_token)


readFromConsole()


