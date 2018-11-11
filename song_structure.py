from random import randint

def structure(song):
    song_lines = song.splitlines()
    hook_lines = []
    hook_type = randint(1, 4)
    hook_reps = randint(2, 4)
    if hook_type == 1:
        for x in range(4):
            random_line = song_lines.pop(randint(0, len(song_lines)-1)) # need a check to make sure song has enough lines
            hook_lines += random_line
    pre_hook_length = len(song_lines)
    for x in range(hook_reps):
        i = pre_hook_length/(hook_reps/(x+1))
        song_lines[i:i] = hook_lines
    '\n'.join(song_lines)

    '''
    20 lines
    4 hook reps
    
    4/1=4
    '''



'''
HOOK TYPES:
*can randomize the length of all of these, but make randomized options make sense in terms of meter
AAAA
ABACADAE 
ABABABAB
ABCD
'''
