#!/usr/bin/env python3

input_file = 'day15_input.txt'
# input_file = 'day15_test.txt'

with open(input_file) as f:
    data = [x.strip() for x in f.readlines()]


def HASH(string):
    number = 0
    for char in string:
        ascii_code = ord(char)
        number += ascii_code
        number *= 17
        number = number % 256
    return number


initialization_seq = data[0].split(',')

segments = []
boxes = {}
counts = {}
for segment in initialization_seq:
    if segment.endswith('-'):
        label = segment[:-1]
        label_hash = HASH(label)
        # print('-', label_hash, label)
        if label in boxes.setdefault(label_hash, []):
            label_index = boxes[label_hash].index(label)
            t = boxes[label_hash].pop(label_index)
            counts[label] = 0
    else:
        label, number = segment.split('=', 1)
        label_hash = HASH(label)
        # print('>', label_hash, label, number)
        if label not in boxes.setdefault(label_hash, []):
            boxes[label_hash].append(label)
        counts[label] = int(number)
        # print('box:', boxes[label_hash])
    segments.append(HASH(segment))

focus_power = 0
for box, contents in boxes.items():
    box_num = box + 1
    if contents:
        for i, lense in enumerate(contents):
            slot = i + 1
            focus_power += box_num * slot * counts[lense]
print('focus power:', focus_power)
