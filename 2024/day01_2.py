#!/usr/bin/env python3
import collections

input_file = 'day01_input.txt'
# input_file = 'day01_sample.txt'

with open(input_file) as f:
    left = []
    right = []
    for line in f.readlines():
        l, r = line.split() 
        left.append(int(l))
        right.append(int(r))
    counts = collections.Counter(right)
    similarity_score = [l * counts[l] for l in left]
    print(sum(similarity_score))

