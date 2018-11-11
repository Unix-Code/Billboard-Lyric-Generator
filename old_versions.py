from random import randint


def separate_lines(lyrics):
    song = ''
    words = lyrics.split(' ')
    line_length = 0
    for i, val in enumerate(words):
        song += words[i] + ' '
        line_length += 1
        if (words[i][-1:] == ',' or words[i][-1:] == '?' or words[i][-1:] == ')') and line_length >= 4:
            song += '\n'
            line_length = 0
        elif line_length >= 10:
            song += '\n'
            line_length = 0
    return song



def add_hooks(song):
    song_lines = song.strip().splitlines()
    hook_lines = ['\n']
    hook_type = randint(1, 4)
    hook_reps = randint(2, 4)
    title_length = randint(1, 3)
    title = ''
    if hook_type == 1:  # ABCD
        for x in range(4):
            random_line = song_lines.pop(
                randint(0, len(song_lines) - 1))  # need a check to make sure song has enough lines
            hook_lines.append(random_line)
        title = generate_title(hook_lines[randint(1, 4)])
    elif hook_type == 2:  # AAAA
        random_line = song_lines.pop(randint(0, len(song_lines) - 1))  # need a check to make sure song has enough lines
        title = generate_title(random_line)
        for x in range(4):
            hook_lines.append(random_line)
    elif hook_type == 3:  # ABACADAE
        main_line = song_lines.pop(randint(0, len(song_lines) - 1))  # need a check to make sure song has enough lines
        title = generate_title(main_line)
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
        title = generate_title(hook_lines[randint(1, 2)])
    hook_lines.append('\n')
    pre_hook_length = len(song_lines)
    offset = 0
    for x in range(hook_reps):
        i = round(pre_hook_length / ((hook_reps + 1) / (x + 1))) + offset
        song_lines[i:i] = hook_lines
        offset += len(hook_lines)
    lyrics = '\n'.join(song_lines)

    return title.upper() + '\n\n' + lyrics


def generate_title(line):
    words = line.split(' ')
    title = words[0:randint(2, 4)]
    return ' '.join(title)
