import sys

def split_subtitles(filename):
    f = open(filename, 'r')

    subtitle_map = {}
    current_language = None

    for l in f:
        if l.startswith('['):
            #This is a new language
            current_language = l
            current_language = current_language.strip('[]\n')
            subtitle_map[current_language] = ''
        else:
            if current_language != None:
                subtitle_map[current_language] += l

    write_map(subtitle_map)

def write_map(m):
    for k in m:
        f = open(k + '.subtitle', 'w')
        for s in m[k].splitlines():
            f.write(s)

split_subtitles(sys.argv[1])
