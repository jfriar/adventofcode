#!/usr/bin/env python3

input_file = 'day1_input.txt'
replacements = {'one': '1',
                'two': '2',
                'three': '3',
                'four': '4',
                'five': '5',
                'six': '6',
                'seven': '7',
                'eight': '8',
                'nine': '9'}

# Ivan's solution:
def find_coords(line):
    left = {line.find(x): i for x, i in replacements.items() if x in line}
    right = {line.rfind(x): i for x, i in replacements.items() if x in line}
    left.update({line.find(i): i for x, i in replacements.items() if i in line})
    right.update({line.rfind(i): i for x, i in replacements.items() if i in line})
    return int(left[min(left)] + right[max(right)])


with open(input_file) as f:
    coords = []
    for line in f.readlines():
        line = line.rstrip()
        _coords = {}
        for i in range(len(line)):
            for search_word, search_int in replacements.items():
                if line[i:].startswith(search_word) or line[i:].startswith(search_int):
                    _coords[i] = search_int
        coords.append(int(_coords[min(_coords)] + _coords[max(_coords)]))
        # coords.append(find_coords(line))
    print(sum(coords))

# 55358 correct
