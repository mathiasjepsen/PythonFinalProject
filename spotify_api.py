import requests
import json
import api_key
import custom_exceptions


def create_playlist(user_id, token, playlist_name, playlist_description):
    url_create_playlist = "https://api.spotify.com/v1/users/" + \
                          f"{user_id}/playlists"
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}"
    }
    body = {
        "name": playlist_name,
        "description": playlist_description
    }
    r = requests.post(url_create_playlist, 
                      headers=headers,
                      data=json.dumps(body))
    # r is a response object                  
    results = r.json()
    #results is a dictionary
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
                 "the necessary rights or is invalid (could have expired)."})


def find_spotify_songs(titles_as_URL, token):
    uris = []
    unknown_songs = []
    for url_title in titles_as_URL:
        url = f"https://api.spotify.com/v1/search?q={url_title}&type=track"
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "Authorization": f"Bearer {token}"
        }
        r = requests.get(url, headers=headers)
        results = r.json()

        try:
            uris.append(results["tracks"]["items"][0]["uri"])
        except KeyError:
            if results["error"]:
                print(results["error"]["message"]) # request crashed, can be because of token invalid
        except IndexError:
            unknown_songs.append(url_title.replace("%20", " ")) #song wasn't found
    return uris, unknown_songs


def add_to_playlist(user_id, uris, token, playlist_id):
    url = f"https://api.spotify.com/v1/users/{user_id}/playlists/" + \ 
          f"{playlist_id}/tracks"                                   #\ means it continues on the line below                                 
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}"
    }
    body = {
        "uris": uris
    }
    requests.post(url, headers=headers,
                       data=json.dumps(body))