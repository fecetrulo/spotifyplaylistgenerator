import os
import json

from spotifyclient import SpotifyClient
from track import Track


def main():
    spotify_client = SpotifyClient(
        os.getenv("SPOTIFY_AUTHORIZATION_TOKEN"), os.getenv("SPOTIFY_USER_ID")
    )

    # get playlist name from user and create playlist
    playlist_name = input("\nWhat's the playlist name? ")
    playlist = spotify_client.create_playlist(playlist_name)
    print(f"\nPlaylist '{playlist.name}' was created successfully.")

    tracks_file = json.load(open("tracks.json"))
    tracks = []
    for t in tracks_file:
        tracks.append(spotify_client.search_track(Track(t["name"], t["artist"])))
        if len(tracks) == 100:
            print(f"\nPopulating playlist with 100 tracks")
            spotify_client.populate_playlist(playlist, tracks)
            tracks.clear()

    print(f"\nPopulating playlist with {len(tracks)} tracks")
    spotify_client.populate_playlist(playlist, tracks)


if __name__ == "__main__":
    main()
