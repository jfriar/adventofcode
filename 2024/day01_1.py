#!/usr/bin/env python3

input_file = 'day01_input.txt'
# input_file = 'day01_sample.txt'

with open(input_file) as f:
    left = []
    right = []
    for line in f.readlines():
        l, r = line.split() 
        left.append(int(l))
        right.append(int(r))
    left.sort()
    right.sort()
    # print(left, right)
    subtracted = [abs(r-l) for l, r in zip(left,right)]
    print(sum(subtracted))

