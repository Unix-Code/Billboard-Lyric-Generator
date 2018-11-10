import requests
import re
from bs4 import BeautifulSoup
from urllib.parse import urlencode
import lyricsgenius as genius

def get_all_lyrics(objs):
    lyrics = [get_lyrics(obj) for obj in objs]
    lyrics = [obj for obj in lyrics if obj is not None]
    return lyrics

def get_lyrics(obj):
    title = obj['Title']
    artist = obj['Artist']

    try:
        api = genius.Genius('5dPz7ZCeg7v8VXj14a9G7WVoVVlK6EakjGC6WCRU-A8dboAM3ktTUVMVQzBUG49_')
        song = api.search_song(title, artist)
        lyrics = re.sub(r'\[.*\]', '', song.lyrics.strip())
        return lyrics
        #print(lyrics)
    except Exception as e:
        print("Couldn't get lyrics from %s" % url)
        return None

if __name__ == '__main__':
    #get_lyrics("https://www.azlyrics.com/lyrics/travisscott/sickomode.html")
    get_lyrics({'Title': 'sicko mode', 'Artist': 'Travis Scott'})
