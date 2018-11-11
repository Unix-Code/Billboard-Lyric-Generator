from random import randint


def structure(song):
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


if __name__ == '__main__':
    manual_song = '''
    1 this is a test song
    2 yeah i said its a test song
    3 these arent real lyrics
    4 they'll be replaced with gibberish
    5 and then some of that gibberish
    6 will become lines of a hook
    7 yeah yeah yeah yeah
    8 we're making some hooks up in this bitch
    9 we at boston hacks
    10 memes are okay
    11 i repeat, this is not a song
    12 i dont even know if my hook generation will work
    13 i gotta make this song pretty damn long
    14 if i want it to be an accurate test example
    15 now that i think of it
    16 i could have just copied and pasted stuff
    17 from the internet
    18 and used that as a song
    19 but at this point im too deep
    20 im just typing a constant stream of consciousness
    21 but i realized the lengths of the lines are kind of irrelevant
    22 so i could
    23 just go
    24 like this
    25 for a
    26 long time
    27 but if
    28 these lines
    29 are chosen as a hook
    30 it would not make much sense
    31 but this song wont make much sense anyway
    32 i just realized that the split string list could
    33 have empty strings in the list as line breaks
    34 but im not sure
    35 okay the song is over
    '''

    gen4_song = '''
    she gotta 50 hundred dollars to me 
I'm on LA But I did turning like your highway
I need everything to find Folgers 
I don't) I've been mad) for you
.40 in the pot A nigga, too, 
I make it out of it you turned 
what's ready for me? 
in the mission Big backend 
and I go, you was about
Or that's more 
I been drilling that you said it 
tickle me I just made zonin' on the same days
Hop with the perfect bars for this word) 
Yeah, pull up in the album like I had a fool in my coupe 
I got that numbers and BET cause y'all both gon' fold
Black on bein' Musk, so hard? 
Man, who's always live for your homies for me 
Yeah, you ain't got lightning harder than my athlete yeah, 
I don't know everything I know that it don't love my be 
or just to love my love (we do it King's different bottles 
Will I keep bent, no testimony (yuh) 
You just the different Side girl, 
y'all give me drips I just switch at sight rappers, 
just get all and light out the favorite radar, 
'til it's way after the furnace
'''
    print(structure(gen4_song))

# 20 lines
# 4 hook reps
#
# 4/1=4, 20/4=5
# 4/2=2, 20/2=10
# 4/3=1.333, 20/1.333=15
#
# 20 lines
# 5 hook reps
# x = 0, 1, 2, 3, 4
#
# 6/1=6, 20/6 = 3.3333
# 6/2=3, 20/3 = 6.6666
# 6/3=2, 20/2 = 10
# 6/4=1.5, 20/1.5 = 13.333
# 6/5=1.2, 20/1.2 = 16.6666


# EPOCH 2 850


# HOOK TYPES:
# *can randomize the length of all of these, but make randomized options make sense in terms of meter
# AAAA
# ABACADAE
# ABCD
# ABABABAB
