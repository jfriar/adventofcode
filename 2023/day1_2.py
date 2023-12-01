#!/usr/bin/env python3
import re

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
        left_coords = {}
        right_coords = {}
        for search_word, search_int in replacements.items():
            if re.search(search_word, line):
                left_coords[line.find(search_word)] = search_int
                right_coords[line.rfind(search_word)] = search_int
            if re.search(search_int, line):
                left_coords[line.find(search_int)] = search_int
                right_coords[line.rfind(search_int)] = search_int

        coords.append(int(left_coords[min(left_coords)] + right_coords[max(right_coords)]))
        # coords.append(find_coords(line))
    print(sum(coords))

# 55358 correct
