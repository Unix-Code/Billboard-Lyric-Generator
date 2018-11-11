import requests
import re
from bs4 import BeautifulSoup
from urllib.parse import urlencode


def get_all_lyrics(objs):
    lyrics = [get_lyrics(obj) for obj in objs]
    lyrics = [obj for obj in lyrics if obj is not None]
    return lyrics

def get_url(obj):
    title = obj['Title']
    artist = obj['Artist']
    q_str = title + " " + artist
    query = urlencode({'q': q_str})
    url = "https://search.azlyrics.com/search.php?%s" % query

    r = requests.get(url)
    r.encoding = 'utf-8'
    content = r.text

    soup = BeautifulSoup(content, 'lxml')
    song = soup.find(string="Song results:")
    song_url = ""
    if (song is not None):
        song = song.find_next("td")
        song_url = song.a['href']
    return song_url
 
def get_lyrics(obj):
    url = get_url(obj)

    if url == "":
        return None

    try:
        r = requests.get(url)
        r.encoding = 'utf-8'
        content = r.text
        soup = BeautifulSoup(content, 'lxml')
        soup = soup.find(class_="ringtone").find_next("div")
        lyrics = soup.text.strip()
        lyrics = re.sub(r'\[.*\]', '', lyrics)
        print(lyrics)
        return lyrics
    
    except Exception as e:
        print("Couldn't get lyrics from %s" % url)

if __name__ == '__main__':
    #get_lyrics("https://www.azlyrics.com/lyrics/travisscott/sickomode.html")
    get_url({'Title': 'sicko mode', 'Artist': 'Travis Scott'})
