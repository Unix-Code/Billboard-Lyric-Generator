import codecs
from random import randint


def add_hooks(song):
    song_lines = song.strip().splitlines()
    hook_lines = ['\n']
    hook_type = randint(1, 4)
    hook_reps = randint(2, 4)
    if hook_type == 1:  # ABCD
        for x in range(4):
            random_line = song_lines.pop(
                randint(0, len(song_lines) - 1))  # need a check to make sure song has enough lines
            hook_lines.append(random_line)
    elif hook_type == 2:  # AAAA
        random_line = song_lines.pop(randint(0, len(song_lines) - 1))  # need a check to make sure song has enough lines
        for x in range(4):
            hook_lines.append(random_line)
    elif hook_type == 3:  # ABACADAE
        main_line = song_lines.pop(randint(0, len(song_lines) - 1))  # need a check to make sure song has enough lines
        for x in range(4):
            random_line = song_lines.pop(
                randint(0, len(song_lines) - 1))  # need a check to make sure song has enough lines
            hook_lines.append(main_line)
            hook_lines.append(random_line)
    elif hook_type == 4:  # ABABABAB
        first_line = song_lines.pop(randint(0, len(song_lines) - 1))  # need a check to make sure song has enough lines
        second_line = song_lines.pop(randint(0, len(song_lines) - 1))  # need a check to make sure song has enough lines
        for x in range(4):
            hook_lines.extend([first_line, second_line])
    hook_lines.append('\n')
    pre_hook_length = len(song_lines)
    offset = 0
    for x in range(hook_reps):
        i = round(pre_hook_length / ((hook_reps + 1) / (x + 1))) + offset
        song_lines[i:i] = hook_lines
        offset += len(hook_lines)
    return '\n'.join(song_lines)


def separate_lines(lyrics):
    song = ''
    lyrics = lyrics.replace(') ', ')\n')
    lines = lyrics.split('\n')
    for i in range(len(lines)):
        lines[i] = lines[i].replace(', ', ',\n')
    lines = '\n'.join(lines).split('\n')
    adding_at_front = False
    for i in range(len(lines)):
        line_words = lines[i].split(' ')
        if len(line_words) > 8:
            num_divs = round(len(line_words)/8)
            for x in range(num_divs):
                if not adding_at_front:
                    song += '\n'
                song += ' '.join(line_words[round(len(line_words)/num_divs*x):round(len(line_words)/num_divs*(x+1))])
                adding_at_front = False
        elif len(line_words) < 3:
            if not adding_at_front:
                song += '\n'
            song += ' '.join(line_words)
            adding_at_front = True
        else:
            if not adding_at_front:
                song += '\n'
            song += ' '.join(line_words)
            adding_at_front = False
    print(song)
    print('~~~~~~~~~~~~~~~~~~``')
    return song
    # for i in range(len(lines)):
    #     line_words = lines[i].split(' ')
    #     if len(line_words) > 8:
    #         num_divs = round(len(line_words)/8)
    #         for x in range(num_divs):
    #             song += '\n' + ' '.join(line_words[round(len(line_words)/num_divs*x):round(len(line_words)/num_divs*(x+1))])
    #     elif len(line_words) < 3:
    #         song += ' '.join(line_words)
    #     else:
    #         song += '\n' + ' '.join(line_words)
    # return song

    # song = ''
    # lyrics = lyrics.replace(', ', ',\n')
    # lines = lyrics.split('\n')
    # for i in range(len(lines)):
    #     line_words = lines[i].split(' ')
    #     if len(line_words) > 8:
    #         num_divs = round(len(line_words)/8)
    #         for x in range(num_divs):
    #             song += '\n' + ' '.join(line_words[round(len(line_words)/num_divs*x):round(len(line_words)/num_divs*(x+1))])
    #     elif len(line_words) < 3:
    #         song += ' '.join(line_words)
    #     else:
    #         song += '\n' + ' '.join(line_words)
    # return song


def trim_ending(lyrics):
    for i in range(50):  # we will always pass in lyrics with more than 50 characters
        char = lyrics[-(i+1)]
        if char == ',' or char == '?' or char == ')':
            return lyrics[:-(i+1)]
    return lyrics


def clean_parens(lyrics):
    words = lyrics.split()
    opened = False
    opened_index = 0
    for i, val in enumerate(words):
        word = words[i]
        if opened:
            if word[-1] == ')':
                opened = False
            elif word[0] == '(':
                words[opened_index] = words[opened_index].replace('(', '')
                opened_index = i
            elif (i - opened_index) > 1:
                words[opened_index] = words[opened_index].replace('(', '')
                opened = False
        else:
            if word[-1] == ')' and word[0] != '(':
                words[i] = words[i].replace(')', '')
            elif word[0] == '(' and word[-1] != ')':
                opened_index = i
                opened = True
    return ' '.join(words)


def get_primer():
    with codecs.open('../corpus/corpus_final.txt', 'r', "utf-8") as f:
        corpus = f.read()
    words = corpus.split()

    # remove conjunctions and non-alphanumeric words from potential primers:
    words = [word for word in words if word.isalnum() and word not in ['and', 'but']]
    return words[randint(0, len(words)-1)]


def get_full_song(lyrics):
    print("started")
    #lyrics = ''
    #with codecs.open('../generated songs/gen15.txt', 'r', "utf-8") as f:
    #    lyrics = f.read()
    return add_hooks(separate_lines(trim_ending(clean_parens(lyrics))))


if __name__ == '__main__':
    lyrics = ''
    with codecs.open('../generated songs/gen15.txt', 'r', "utf-8") as f:
       lyrics = f.read()
    print(add_hooks(separate_lines(trim_ending(clean_parens(lyrics)))))

