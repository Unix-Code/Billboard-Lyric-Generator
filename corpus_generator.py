from billboard import ChartData
from lyrics import get_all_lyrics
import codecs

# chart = ChartData('rap-song', date='2018-11-10')
# print(chart)
# info[4]['Artist']

def convert_hit(hit):
    hit = list(hit)
    hit = {list(hit[0])[0]: list(hit[0])[1],
           list(hit[1])[0]: list(hit[1])[1]}
    return hit

def trim_features(artist):
    return artist.split('Featuring')[0]

def get_songs(chart, stop_month):
    hits = set()

    while chart.previousDate[:7] != stop_month:
        print(chart.previousDate)
        results = [frozenset(({'Title': song.title.strip(), 'Artist': trim_features(song.artist).strip()}).items()) for song in chart]
        hits.update(results)
        chart = ChartData(chart.name, chart.previousDate)

    hits = [convert_hit(hit) for hit in list(hits)]
    for hit in hits:
        print(hit)
    print(str(len(hits)) + ' entries found')

    return hits

def remove_brackets(lyrics):
    filtered_lyrics = ''
    for s in lyrics.split('['):
        splitted = s.split(']')
        if len(splitted) > 1:
            filtered_lyrics += splitted[1]
    return filtered_lyrics

def run():
    chart = ChartData('r-b-hip-hop-songs')
    stop_month = '2016-12'
    songs = get_songs(chart, stop_month)
    corpus = '\n\n'.join(get_all_lyrics(songs))
    with codecs.open('corpus.txt', 'w', "utf-8") as f:
        f.write(corpus)

if __name__ == '__main__':
    run()


