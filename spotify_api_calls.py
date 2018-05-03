import requests
import json
import api_key


def create_playlist():
    user_id = "serenitymusic97"
    url_create_playlist = f"https://api.spotify.com/v1/users/{user_id}/playlists"
    headers = {"Accept": "application/json",
               "Content-Type": "application/json",
               "Authorization": f"Bearer {api_key.SPOTIFY_TOKEN}"}
    body = {
        "name": "Test playlist",
        "description": "Test desc"
}
    r = requests.post(url_create_playlist, headers=headers, data=json.dumps(body))
    results = r.json()
    print(results)

def add_to_playlist(uris):
    user_id = "serenitymusic97"
    playlist_id = "4nhErVvTyR25yVO0oKV3OT"
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

