with open('wordcountinput.txt') as f:
    counts = {'characters':0,
              'words':0,
              'lines':0}
    unique_words = set()

    for l in f:
        counts['lines'] += 1
        counts['characters'] =+ len(l)
        counts['words'] =+ len(l.split())

        unique_words.update(l.split())

    counts['unique_words'] = len(unique_words)

    for k, v in counts.items():
        print (f'{k}: {v}')
