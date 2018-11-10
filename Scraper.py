from billboard import ChartData

# chart = ChartData('rap-song', date='2018-11-10')
# print(chart)
# info[4]['Artist']

def get_url(obj):
    url = ''
    return url

def get_lyrics(url):
    lyrics = ''
    return lyrics

def trim_features(artist):
    return artist.split('Featuring')[0]

def get_songs(chart):
    hits = []

    while chart.previousDate[0:4] != '2013':
        for song in chart:
            result = {'Title': song.title, 'Artist': trim_features(song.artist)}
            if result not in hits:
                hits += [result]
        chart = ChartData(chart.name, chart.previousDate)

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

# '\n\n'.join()

def run():
    corpus = ''
    chart = ChartData('r-b-hip-hop-songs')
    get_songs(chart)

    for song in get_songs(chart):
        corpus += get_lyrics(get_url(song)) + '\n\n'



if __name__ == '__main__':
    run()


