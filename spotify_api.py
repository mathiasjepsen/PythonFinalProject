import requests
import json
import api_key


def create_playlist(user_ID, playlist_Name, playlist_Description):
    global user_id 
    global playlist_name
    global playlist_description
    user_id = user_ID
    playlist_name = playlist_Name
    playlist_description = playlist_Description
    url_create_playlist = f"https://api.spotify.com/v1/users/{user_id}/playlists"
    headers = {"Accept": "application/json",
               "Content-Type": "application/json",
               "Authorization": f"Bearer {api_key.SPOTIFY_TOKEN}"}
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


