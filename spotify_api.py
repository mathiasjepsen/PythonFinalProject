import requests
import json
import api_key
from bs4 import BeautifulSoup



def verify_account_info(username, TOKEN):
    url = f"https://api.spotify.com/v1/users/{username}"

    headers = {"Accept": "application/json",
                "Content-Type": "application/json",
                "Authorization": f"Bearer {TOKEN}"}

    r = requests.get(url, headers=headers)
    results = r.json()
    try:
        print(results["error"]["message"])
    except KeyError:
        print("good")


def create_playlist(ID, TOKEN, playlist_name, playlist_description):
    global user_id
    user_id = ID

    url_create_playlist = f"https://api.spotify.com/v1/users/{user_id}/playlists"
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": f"Bearer {TOKEN}"
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
        return create_playlist(user_id, TOKEN, playlist_name, playlist_description)


def add_to_playlist(uris, TOKEN, playlist_id):
    url = f"https://api.spotify.com/v1/users/{user_id}/playlists/{playlist_id}/tracks"

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": f"Bearer {TOKEN}"
    }

    body = {
        "uris": uris
    }

    requests.post(url, headers=headers,
                       data=json.dumps(body))



