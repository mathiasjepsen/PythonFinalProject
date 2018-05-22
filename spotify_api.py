import requests
import json
import api_key


def create_playlist(id, playlist_name, playlist_description):
    global user_id
    user_id = id

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


# def readFromConsole():
#     username = input("Hello Sir, may I ask for your username please:")
#     playlist_name = input(
#         "Now I will ask you for the name you want to provide for the playlist:")
#     playlist_description = input("Description of the playlist:")
#     token = input("Your token:")
#     return username, playlist_name, playlist_description, token


# readFromConsole()
