import requests
import json
import api_key
import custom_exceptions
from bs4 import BeautifulSoup


def create_playlist(ID, TOKEN, playlist_name, playlist_description):
    global user_id
    user_id = ID

    url_create_playlist = "https://api.spotify.com/v1/users/" + \
                          f"{user_id}/playlists"
    print(url_create_playlist)
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
        if results["error"]["status"] == 403:
            raise  custom_exceptions.WrongUsernameException(
                {"message":"The provided username does not match " + \
                 "the provided token or is incorrect."})
        elif results["error"]["status"] == 401:
            raise  custom_exceptions.InvalidTokenException(
                {"message":"The token provided does not include " + \
                 "the necessary rights or is invalid."})


def add_to_playlist(uris, TOKEN, playlist_id):
    url = f"https://api.spotify.com/v1/users/{user_id}/playlists/" + \
          f"{playlist_id}/tracks"

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



