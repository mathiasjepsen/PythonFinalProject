import pytube
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from tqdm import tqdm


playlist_link = "https://www.youtube.com/playlist?list=PLBILG-T6e7eBKFRUCC05ErhBfJ3gPVBkB"
browser = webdriver.Chrome()
browser.get(playlist_link)
browser.implicitly_wait(3)

stats = browser.find_element_by_id("stats")
num_of_videos = stats.text.split()[0]
play_all_button = browser.find_element_by_xpath('//*[@class="style-scope ytd-playlist-sidebar-primary-info-renderer"]')
play_all_button.click()
sleep(2)
mute_button = browser.find_element_by_xpath('//*[@class="ytp-mute-button ytp-button"]')
mute_button.click()
sleep(2)

titles = []
for _ in tqdm(range(int(num_of_videos))):
    if not browser.find_elements_by_xpath('//*[@class="reason style-scope ytd-player-error-message-renderer"]'):
        title = pytube.YouTube(browser.current_url).title
        titles.append(title)
        next_button = browser.find_element_by_xpath('//*[@class="ytp-next-button ytp-button"]')
        browser.execute_script("arguments[0].click();", next_button)
    else:
        title = browser.find_element_by_xpath('//*[@class="style-scope ytd-video-primary-info-renderer"]').text.splitlines()[0]
        titles.append(title)
        sleep(5)
    
print(titles)

# search_field = browser.find_element_by_id('search')
# search_field.send_keys('Kim Larsen playlist')
# search_field.submit()
# sleep(3)

#page_source = browser.page_source
#print(page_source)


#class="yt-simple-endpoint style-scope ytd-playlist-renderer"
#    href="/watch?v=prgsiq1Z8wM&list=PL4xuvJvndzN5tg4adjUv6ORp2Rszd9L1K"