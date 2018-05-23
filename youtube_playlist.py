import pytube
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from tqdm import tqdm
import requests
import json
import api_key
import spotify_api
import bs4


def init(playlist_link):
    global num_of_videos
    global browser
    browser = webdriver.Chrome()
    browser.get(playlist_link)

    stats = browser.find_element_by_id("stats")
    num_of_videos = stats.text.split()[0]
    play_all_button = browser.find_element_by_xpath(
        '//*[@class="style-scope ytd-playlist-sidebar-primary-info-renderer"]')
    play_all_button.click()
    sleep(2)
    mute_button = browser.find_element_by_xpath(
        '//*[@class="ytp-mute-button ytp-button"]')
    mute_button.click()


def scrape_titles():
    titles = []
    for _ in tqdm(range(int(num_of_videos))):
        title = browser.find_element_by_xpath(
            '//*[@class="style-scope ytd-video-primary-info-renderer"]') \
            .text.splitlines()[0]        
        titles.append(title)
        next_button = browser.find_element_by_xpath(
            '//*[@class="ytp-next-button ytp-button"]')
        browser.execute_script("arguments[0].click();", next_button) 
        #next_button.click()
        sleep(2) # If we can find a way to have this be more dynamic, 
                 # and not hard-coded to 2, that'd be nice

    return titles
   

def find_spotify_songs(titles_as_URL):
    uris = []
    unknown_songs = []
    for url_title in titles_as_URL:
        url = f"https://api.spotify.com/v1/search?q={url_title}&type=track"

        headers = {"Accept": "application/json",
                "Content-Type": "application/json",
                "Authorization": f"Bearer {api_key.SPOTIFY_TOKEN}"}

        r = requests.get(url, headers=headers)
        results = r.json()

        try:
            uris.append(results["tracks"]["items"][0]["uri"])
        except KeyError:
            if results["error"]:
                print(results["error"]["message"])
        except IndexError:
            unknown_songs.append(url_title.replace("%20", " "))

    return (uris, unknown_songs)


def main():
    print("Please enter the following information in order to continue:")
    playlist_link = input("The link to the playlist: \n> ")
    spotify_username = input("Spotify username: \n> ")
    playlist_name = input("Playlist name: \n> ")
    playlist_description = input("Playlist description: \n> ")

    init(playlist_link)

    titles = scrape_titles()
    titles_as_URL = [title.replace(" ", "%20") for title in titles]

    uris, unknown_songs = find_spotify_songs(titles_as_URL)

    playlist_id = spotify_api.create_playlist(spotify_username, 
                                              playlist_name, 
                                              playlist_description)
    
    spotify_api.add_to_playlist(uris, playlist_id)

    print("The following songs couldn't be added to the playlist: ")
    for song in unknown_songs:
        print(song)

if __name__ == "__main__":
    main()

