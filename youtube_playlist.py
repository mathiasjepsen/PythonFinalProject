import pytube
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from tqdm import tqdm
import requests
import json
import api_key
import spotify_api_calls

playlist_link = "https://www.youtube.com/playlist?list=PLBILG-T6e7eDeszgpd2qZTAcRIHEvn4ES"
browser = webdriver.Chrome()
browser.get(playlist_link)
browser.implicitly_wait(3)

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
    if not browser.find_elements_by_xpath('//*[@class="reason style-scope ytd-player-error-message-renderer"]'):
        title = pytube.YouTube(browser.current_url).title
        titles.append(title)
        next_button = browser.find_element_by_xpath(
            '//*[@class="ytp-next-button ytp-button"]')
        #browser.execute_script("arguments[0].click();", next_button)
        next_button.click()
    else:
        title = browser.find_element_by_xpath(
            '//*[@class="style-scope ytd-video-primary-info-renderer"]').text.splitlines()[0]
        titles.append(title)
        sleep(5)


titles_to_URL = []
for title in titles:
    title_split = title.split()
    title_url = ""
    for idx, word in enumerate(title_split):
        if(idx != len(title_split) - 1) :
            title_url += word + "%20"
        else :
            title_url += word
    titles_to_URL.append(title_url)     
    print(titles_to_URL)


uris = []
for url_title in titles_to_URL:
    url = f"https://api.spotify.com/v1/search?q={url_title}&type=track"
    headers = {"Accept": "application/json",
            "Content-Type": "application/json",
            f"Authorization": "Bearer {api_key.SPOTIFY_KEY}"}

    r = requests.get(url, headers=headers)
    results = r.json()
    print(results)
    uris.append(results["tracks"]["items"][0]["uri"])

spotify_api_calls.create_playlist()
spotify_api_calls.add_to_playlist(uris)


# for id in ids:
#     url = f"https://api.spotify.com/v1/tracks/{id}"
#     query = {"Accept": "application/json",
#             "Content-Type": "application/json",
#             "Authorization": "Bearer "}

#     r = requests.get(url, headers=query)
#     results = r.json()
#     print(results)
