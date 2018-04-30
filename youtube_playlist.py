import pytube
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


base_url = 'http://www.youtube.com'
browser = webdriver.Firefox()
browser.get(base_url)
browser.implicitly_wait(3)

search_field = browser.find_element_by_id('search')
search_field.send_keys('Kim Larsen playlist')
search_field.submit()
sleep(3)

page_source = browser.page_source
print(page_source)

link = "https://www.youtube.com/watch?v=prgsiq1Z8wM&list=PL4xuvJvndzN5tg4adjUv6ORp2Rszd9L1K"

video = pytube.YouTube(link)
title = video.title

print(title)


#class="yt-simple-endpoint style-scope ytd-playlist-renderer"
#    href="/watch?v=prgsiq1Z8wM&list=PL4xuvJvndzN5tg4adjUv6ORp2Rszd9L1K"