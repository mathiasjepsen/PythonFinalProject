import requests
import json
import api_key


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
    print(results["name"], results["id"])
    return results["id"]


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
    r = requests.get(url, headers = headers,
                params = params)
    data = r.json()
    print(data["id"], data["name"])

def search(q, typeSearch):
    url = f"https://api.spotify.com/v1/search"
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key.SPOTIFY_TOKEN}"
    }
    params = {
        "q": q,
        "type": typeSearch
    }
    r = requests.get(url, headers = headers,
                params = params)
    data = r.json()
    print(data)



def readFromConsole():
    # input_name = input("Hello Sir, may I ask for your username please:")
    # input_playlistname = input("Now I will ask you for the name you want to provide for the playlist:")
    # input_description = input("Description of the playlist:")
    # print("values you've entered:" + input_name +
    #       input_playlistname + input_description)
    # create_playlist(input_name, input_playlistname,
    #                 input_description)
    # input_id = input("Provide a playlist id in case you want to search for it:")
    #get_playlist(input_id)
    input_q = input("provide a name of an item you are searching for:")
    input_type = input("provide a category album/artist/playlist/track:")
    search(input_q, input_type)


readFromConsole()
