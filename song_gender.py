import requests
import json
import api_key
from bs4 import BeautifulSoup
from collections import Counter


def search(item_name, item_type, token):
    url = f"https://api.spotify.com/v1/search"
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}"
    }
    params = {
        "q": item_name,
        "type": item_type
    }
    r = requests.get(url, headers=headers,
                          params=params)
    data = r.json()
    tracks = data["tracks"]["items"]
    return [(track["name"], track["artists"][0]["name"]) for track in tracks]


def request_song_info(song_title, artist_name):
    url = 'https://api.genius.com'
    headers = {'Authorization': 'Bearer ' +
               api_key.GENIUS_TOKEN}
    search_url = url + '/search'
    data = {'q': song_title + ' ' + artist_name}
    response = requests.get(search_url, data=data, headers=headers)
    return response


def scrap_song_url(url):
    page = requests.get(url)
    html = BeautifulSoup(page.text, 'html.parser')
    lyrics = html.find('div', class_='lyrics').get_text()
    return lyrics


def read_from_console():
    input_q = input("provide a name of an item you are searching for: \n> ")
    input_type = input("provide a category album/artist/playlist/track: \n> ")
    token = input("Spotify authentification token: \n> ")
    tracks_info = search(input_q, input_type, token)
    for song, artist in tracks_info:
        print(f"{song}  -  {artist}")

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

    myDict = {
            "male": ["uh", "ah", "yeah", "mean", "you", "wife", "noise", "man", "hey", "pretty", "the",
                        "a", "of", "shit", "sort", "cool", "i", "like", "what", "guy", "there", "bucks"],
            "female": ["mhm", "husband", "and", "my", "oh", "she", "we", "um",
                        "have", "kids", "he", "her", "children", "because", "so",
                        "yes", "daughter", "gosh", "goodness", "son", "home", "too", "wow", "uh-huh"]
    }

    key_list = []
    for key in myDict.keys():
        for value in myDict[key]:
            if value in lyrics:
                key_list.append(key)

    if key_list.count("male") > key_list.count("female"):
        print("Seems like this song favours male specific words")
    elif key_list.count("female") > key_list.count("male"):
        print("Seems like this songs favour female specific words")
    else:
        print("Well well well, it's a draw")
    print ("Number of male words: ", key_list.count("male"), "Number of female words: ", key_list.count("female"))

if __name__ == "__main__":
    read_from_console()