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
    r = requests.get(url, headers=headers,
                     params=params)
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
    r = requests.get(url, headers=headers,
                     params=params)
    data = r.json()
    tracks = data["tracks"]["items"]
    for track in tracks:
        dict = {
            "song_title": track["name"],
            "artist_name": track["artists"][0]["name"]
        }
        # print(track["name"])
        # print("------------------------------------------")
        # print(track["artists"][0]["name"])
        print(dict)
    return dict


def request_song_info(song_title, artist_name):
    base_url = 'https://api.genius.com'
    headers = {'Authorization': 'Bearer ' +
               'ccHDzjsPAnwWcOAo2fS5Kb5cH9BFLqsryi5r0a6p3flgb_B3g8qPguO68A3NZTZJ'}
    search_url = base_url + '/search'
    data = {'q': song_title + ' ' + artist_name}
    response = requests.get(search_url, data=data, headers=headers)
    results = response.json()
    # print(results)
    return response


def scrap_song_url(url):
    page = requests.get(url)
    html = BeautifulSoup(page.text, 'html.parser')
    [h.extract() for h in html('script')]
    lyrics = html.find('div', class_='lyrics').get_text()

    return lyrics


def readFromConsole():
    # input_name = input("Hello Sir, may I ask for your username please:")
    # input_playlistname = input("Now I will ask you for the name you want to provide for the playlist:")
    # input_description = input("Description of the playlist:")
    # print("values you've entered:" + input_name +
    #       input_playlistname + input_description)
    # create_playlist(input_name, input_playlistname,
    #                 input_description)
    # input_id = input("Provide a playlist id in case you want to search for it:")
    # get_playlist(input_id)
    input_q = input("provide a name of an item you are searching for:")
    input_type = input("provide a category album/artist/playlist/track:")
    search(input_q, input_type)
    input_artist = input("Choose an artist:")
    response = request_song_info(input_q, input_artist)
    json = response.json()
    remote_song_info = None

    for hit in json['response']['hits']:
        if input_artist.lower() in hit['result']['primary_artist']['name'].lower():
            remote_song_info = hit
            break
    # Extract lyrics from URL if the song was found
    if remote_song_info:
        song_url = remote_song_info['result']['url']
        lyrics = scrap_song_url(song_url)

    print(lyrics)
    myDict = {
            "male": ["fuck", "her", "she", "gun", "car", "lol"],
            "female": ["him", "he", "skirt", "shop", "love"]
        }

    key_list = []
    for key in myDict.keys():
        for value in myDict[key]:
            if value in lyrics:
                key_list.append(key)
    print(key_list)
    if key_list.count("male") > key_list.count("female"):
        print("it contains more male shit")
    else:
        print("contains more female shit")


readFromConsole()
