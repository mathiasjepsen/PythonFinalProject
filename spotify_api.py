import requests
import json
import api_key

global user_id
global playlist_name
global playlist_description

def create_playlist(user_id, playlist_name, playlist_description):
    user_id = user_id
    playlist_name = playlist_name
    playlist_description = playlist_description
    url_create_playlist = f"https://api.spotify.com/v1/users/{user_id}/playlists"
    headers = {"Accept": "application/json",
               "Content-Type": "application/json",
               "Authorization": f"Bearer {api_key.SPOTIFY_TOKEN}"}
    body = {
        "name": playlist_name,
        "description": playlist_description
    }
    r = requests.post(url_create_playlist, headers=headers, data=json.dumps(body))
    results = r.json()
    print(results)
    # playlist_id = 


def add_to_playlist(uris, playlist_id):
    url = f"https://api.spotify.com/v1/users/{user_id}/playlists/{playlist_id}/tracks"
    headers = {"Accept": "application/json",
               "Content-Type": "application/json",
               "Authorization": f"Bearer {api_key.SPOTIFY_TOKEN}"}
    body = {
        "uris": uris
    }
    r = requests.post(url, headers=headers,
                      data=json.dumps(body))
    results = r.json()
    print(results)

