from config import CONFIG
import requests
import json
import sys

# playlist_name = 'chill_vibez_effortless'
playlist_name = sys.argv[1]

r = requests.get(f"http://api.soundcloud.com/resolve?url=https://soundcloud.com/{CONFIG['SOUNDCLOUD_USERNAME']}/sets/{playlist_name}&client_id={CONFIG['CLIENT_ID']}")

tracks = r.json()['tracks']

with open(f'./tracklists/{playlist_name}_tracklist.txt', 'w+') as f:
    for track in tracks:
        formatted_track = f"@{track['user']['permalink']} :: {track['user']['username']} :: {track['title']}\n"
        f.write(formatted_track)
