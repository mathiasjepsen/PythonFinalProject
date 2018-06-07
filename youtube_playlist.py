from time import sleep
from selenium import webdriver
from tqdm import tqdm
import requests
import json
import api_key
import spotify_api
import custom_exceptions


def init(playlist_link):
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
    return browser, num_of_videos


def scrape_titles(browser, num_of_videos):
    titles = []
    for _ in tqdm(range(int(num_of_videos))): #num_of_videos is a string scrapped from page
        title = browser.find_element_by_xpath(
            '//*[@class="style-scope ytd-video-primary-info-renderer"]') \
            .text.splitlines()[0]        
        titles.append(title)
        next_button = browser.find_element_by_xpath(
            '//*[@class="ytp-next-button ytp-button"]')
        browser.execute_script("arguments[0].click();", next_button) #execute a script, work even if an add, because it is in the DOM, javascript can access the DOM
                                                                    #the first parameter is the javascript script, the following
                                                                    #ones are arguments[], so our next_button is arguments[0], and our javascript is .click() on it
        #next_button.click() this simulate a click of the button, but if there is an add it doesn't work, the button is in the DOM but is hidden to the user at that time
        sleep(2) 
    browser.close()
    return titles


def main():
    print("\nPlease enter the following information in order to continue:")
    playlist_link = input("The link to the playlist: \n> ")

    while "/playlist?list=" not in playlist_link:
        print("Please enter a valid playlist URL.")
        playlist_link = input("The link to the playlist: \n> ")

    browser, num_of_videos = init(playlist_link)

    titles = scrape_titles(browser, num_of_videos)
    titles_as_URL = [title.replace(" ", "%20") for title in titles]

    spotify_username = input("Spotify username: \n> ")
    spotify_api_token = input("Spotify authentification token: \n> ")

    playlist_name = input("Playlist name: \n> ")
    playlist_description = input("Playlist description: \n> ")
    
    while True:
        try:
            playlist_id = spotify_api.create_playlist(spotify_username, 
                                                      spotify_api_token,
                                                      playlist_name, 
                                                      playlist_description)
            break
        except custom_exceptions.WrongUsernameException as e:
            print(e.args[0]["message"])
            spotify_username = input("Spotify username: \n> ")
        except custom_exceptions.InvalidTokenException as e:
            print(e.args[0]["message"])
            spotify_api_token = input("Spotify authentification token: \n> ")

    uris, unknown_songs = spotify_api.find_spotify_songs(titles_as_URL, spotify_api_token)

    spotify_api.add_to_playlist(spotify_username, uris, spotify_api_token, playlist_id)

    if len(unknown_songs) > 0:
        print("The following songs couldn't be added to the playlist:")
        for song in unknown_songs:
            print(song)


if __name__ == "__main__":
    main()

