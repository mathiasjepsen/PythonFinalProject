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

    male_word_list = ["uh", "ah", "yeah", "mean", "you", "wife", "noise", "man", "hey", "pretty", "the",
                       "a", "of", "shit", "sort", "cool", "i", "like", "what", "guy", "there", "bucks", "nigga"]
    female_word_list = ["mhm", "husband", "and", "my", "oh", "she", "we", "um",
                         "have", "kids", "he", "her", "children", "because", "so",
                         "yes", "daughter", "gosh", "goodness", "son", "home", "too", "wow", "uh-huh"]

    male_word_count = {}
    female_word_count = {}

    for word in lyrics.split():
        if word in male_word_list:
            male_word_count.setdefault(word, 0)
            male_word_count[word] += 1
        elif word in female_word_list:
            female_word_count.setdefault(word, 0)
            female_word_count[word] += 1
    print(male_word_count)
    print(female_word_count)
    if sum(male_word_count.values()) > sum(female_word_count.values()):
        print("Seems like this song favours male specific words")
    elif sum(male_word_count.values()) < sum(female_word_count.values()):
        print("Seems like this songs favour female specific words")
    else:
        print("Well well well, it's a draw")


if __name__ == "__main__":
    read_from_console()
