import requests
import json
import api_key
from bs4 import BeautifulSoup


def create_playlist(ID, playlist_name, playlist_description):
    global user_id
    user_id = ID

    url_create_playlist = f"https://api.spotify.com/v1/users/{user_id}/playlists"
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key.SPOTIFY_TOKEN}"
    }

    body = {
        "name": playlist_name,
        "description": playlist_description
    }

    r = requests.post(url_create_playlist, 
                      headers=headers,
                      data=json.dumps(body))
    results = r.json()

    try:
        return results["id"]
    except KeyError:
        print("Invalid user ID, please input again.")
        user_id = input(">")
        return create_playlist(user_id, playlist_name, playlist_description)


def add_to_playlist(uris, playlist_id):
    url = f"https://api.spotify.com/v1/users/{user_id}/playlists/{playlist_id}/tracks"

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key.SPOTIFY_TOKEN}"
    }

    body = {
        "uris": uris
    }

    requests.post(url, headers=headers,
                       data=json.dumps(body))


def get_playlist(playlist_id):
    url = f"https://api.spotify.com/v1/users/{user_id}/playlists/{playlist_id}"
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key.SPOTIFY_TOKEN}"
    }
    params = {
        "playlist_id": playlist_id
    }
    r = requests.get(url, headers=headers,
                     params=params)
    data = r.json()
    print(data["id"], data["name"])

