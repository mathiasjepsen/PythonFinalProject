# PythonFinalProject

### Ideas
1. Convert a YouTube playlist to a Spotify playlist - webscraping and Selenium 
2. AI Art with Style Transfer using Keras 
       https://medium.com/mlreview/making-ai-art-with-style-transfer-using-keras-8bb5fa44b216
3. A program to process and visualize information that facebook has collected about you. 

## Youtube -> Spotify Playlist Converter
### Steps required
1. Figure out which HTML element(s) on the page we need to scrape.
2. Use Selenium to automate the process for us, which will require knowing which button to click to skip forward in the playlist.
3. Figure out how we deal with potential ads on the page, and if it's even necessary. Maybe we don't even have to bother.
4. Compile all the song titles into a list in Python, and then JSONify it.
5. Read up on the Spotify API (https://beta.developer.spotify.com/documentation/web-api/) to learn how to use it properly.
6. Use the Spotify API to make a POST request with the song titles, hopefully creating a new playlist :P
