# SpotifyPlaylist
This code scrapes the top 100 songs from Billboard for a given date, searches for them on Spotify

This Python code uses BeautifulSoup to scrape a list of Billboard Top 100 songs from a specified date, and then uses the Spotipy library to search for and retrieve the Spotify URIs of each song. 
It then creates a new Spotify playlist with the name "YYYY-MM-DD Billboard 100" and adds the retrieved songs to the playlist. 
The playlist is created as private by default. The user is required to authorize the application using the SpotifyOAuth authentication method.
