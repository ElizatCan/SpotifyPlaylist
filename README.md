# SpotifyPlaylist
This code scrapes the top 100 songs from Billboard for a given date, searches for them on Spotify

This Python code uses BeautifulSoup to scrape a list of Billboard Top 100 songs from a specified date, and then uses the Spotipy library to search for and retrieve the Spotify URIs of each song. 
It then creates a new Spotify playlist with the name "YYYY-MM-DD Billboard 100" and adds the retrieved songs to the playlist. 
The playlist is created as private by default. The user is required to authorize the application using the SpotifyOAuth authentication method.


To use this code, user would need to do the following:
-Install the required libraries by running pip install spotipy beautifulsoup4 requests in their terminal or command prompt.
-Create a Spotify developer account and register an application to obtain a Client ID and Client Secret.
-Replace the values for Client_ID, Client_Secret, Redirect_Url, Cache_path, and Scope with your own values.
-Run the script and input the desired date in the format YYYY-MM-DD when prompted.
-If the user has not authenticated with Spotify before, they will be prompted to do so and will need to follow the instructions in the browser window that opens.
-The script will then search for the top 100 songs on the Billboard chart for the input date and add them to a new private playlist in the user's Spotify account with the name {date} Billboard 100.
