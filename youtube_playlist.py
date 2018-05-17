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


playlist_link = "https://www.youtube.com/playlist?list=PLBILG-T6e7eBKFRUCC05ErhBfJ3gPVBkB"
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
sleep(2)


titles = []
for _ in tqdm(range(int(num_of_videos))):
    if browser.find_element_by_xpath('//*[@class="ytp-next-button ytp-button"]'):
        print("DIDN'T FIND")
        title = browser.find_element_by_xpath(
            '//*[@class="style-scope ytd-video-primary-info-renderer"]') \
            .text.splitlines()[0]        
        titles.append(title)
        next_button = browser.find_element_by_xpath(
            '//*[@class="ytp-next-button ytp-button"]')
        browser.execute_script("arguments[0].click();", next_button) 
        #next_button.click()
        sleep(2)
    else:
        print("IN ELSE BLOCK")
        title = browser.find_element_by_xpath(
            '//*[@class="style-scope ytd-video-primary-info-renderer"]') \
            .text.splitlines()[0]
        titles.append(title)
        sleep(5)


titles_to_URL = [title.replace(" ", "%20") for title in titles]


# titles_to_URL = []
# for title in tqdm(titles):
#     title_split = title.split()
#     title_url = ""
#     for idx, word in enumerate(title_split):
#         if(idx != len(title_split) - 1) :
#             title_url += word + "%20"
#         else :
#             title_url += word
#     titles_to_URL.append(title_url)     


uris = []
unknown_songs = []
for url_title in titles_to_URL:
    url = f"https://api.spotify.com/v1/search?q={url_title}&type=track"

    headers = {"Accept": "application/json",
               "Content-Type": "application/json",
               "Authorization": f"Bearer {api_key.SPOTIFY_TOKEN}"}

    r = requests.get(url, headers=headers)
    results = r.json()
    try:
        uris.append(results["tracks"]["items"][0]["uri"])
    except KeyError:
        unknown_songs.append(url_title.replace("%20", " "))
    except IndexError:
        print(url_title)
        print(results)


playlist_id = spotify_api.create_playlist("113963150", 
                                          "Awesome Test Playlist", 
                                          "Test Description")

spotify_api.add_to_playlist(uris, playlist_id)


