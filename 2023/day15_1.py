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
for segment in initialization_seq:
    # print('segment:', segment, 'HASH:', HASH(segment))
    segments.append(HASH(segment))
print()
print(sum(segments))
