# Spotify Playlist Generator

A simple Python application to create custom Spotify playlists using the Spotify Web API, based on a list of tracks.

## Install

Install the necessary Python packages by running:

`$ pip install -r requirements.txt`

## Run

- Add the musics to the file `tracks.json`

- Export the environment variables:

`$ export SPOTIFY_AUTHORIZATION_TOKEN=value_grabbed_from_spotify`

`$ export SPOTIFY_USER_ID=value_grabbed_from_spotify`

- Run the entry-point script and follow the console instructions:

`$ python createplaylist.py`
