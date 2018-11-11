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
    lines = lyrics.replace(', ', ',\n').split('\n')
    for i, line in enumerate(lines):
        line_words = line.split(' ')
        if len(line_words) > 10:
            lines.insert(i + 1, line_words[10:])
    # for i, line in enumerate(lines):
    #     # print(str(len(line.split(' '))))
    #     if len(line) < 15 and i < len(lines) - 1:
    #         lines[i + 1] += ' ' + line
    #     elif len(line.split(' ')) > 10 and i < len(lines) - 1:
    #         tmp = line.split(' ')
    #         # print(tmp[10:])
    #         lines[i + 1] += ' ' + ' '.join(tmp[10:])
    #         song += '\n' + ' '.join(tmp[:10])
    #     else:
    #         song += '\n' + line
    return lines

    # song = ''
    # words = lyrics.split()
    #
    # line_length = 0
    # for i, val in enumerate(words):
    #     song += words[i] + ' '
    #     line_length += 1
    #     if (words[i][-1:] == ',' or words[i][-1:] == '?' or words[i][-1:] == ')') and line_length >= 4:
    #         song += '\n'
    #         line_length = 0
    #     elif line_length >= 10:
    #         song += '\n'
    #         line_length = 0



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


def run():
    lyrics = ''
    with codecs.open('../generated songs/gen15.txt', 'r', "utf-8") as f:
        lyrics = f.read()
    print(separate_lines(trim_ending(clean_parens(lyrics))))
    # print(add_hooks(separate_lines(trim_ending(clean_parens(lyrics)))))


if __name__ == '__main__':
   run()

