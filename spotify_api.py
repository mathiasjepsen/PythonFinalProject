import requests
import json
import api_key
from bs4 import BeautifulSoup


class WrongUsernameException(Exception):
    pass

class InvalidTokenException(Exception):
    pass


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
        status = results["error"]["status"]
        if status == 403:
            raise  WrongUsernameException({"message":"the provided username does not match Token or is incorrect"})
        elif status == 401:
            raise  InvalidTokenException({"message":"the TOKEN provided does not include necessary rights or is invalid"})
    except KeyError:
        return results["id"]
        


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



