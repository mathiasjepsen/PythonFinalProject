import requests
import json
import api_key
from bs4 import BeautifulSoup


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
        print(dict)
    return dict


def request_song_info(song_title, artist_name):
    base_url = 'https://api.genius.com'
    headers = {'Authorization': 'Bearer ' +
               'ccHDzjsPAnwWcOAo2fS5Kb5cH9BFLqsryi5r0a6p3flgb_B3g8qPguO68A3NZTZJ'}
    search_url = base_url + '/search'
    data = {'q': song_title + ' ' + artist_name}
    response = requests.get(search_url, data=data, headers=headers)
    return response


def scrap_song_url(url):
    page = requests.get(url)
    html = BeautifulSoup(page.text, 'html.parser')
    [h.extract() for h in html('script')]
    lyrics = html.find('div', class_='lyrics').get_text()

    return lyrics


def readFromConsole():
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
    if key_list.count("female") > key_list.count("male"):
        print("contains more female shit")
    else:
        print("it's a draw bruh")


readFromConsole()
