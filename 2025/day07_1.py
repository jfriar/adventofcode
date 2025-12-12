#!/usr/bin/env python3

import re

input_file = 'day07_input.txt'
#input_file = 'day07_sample.txt'

tachyon_beams = set()
split_count = 0
with open(input_file) as f:
    for line in f.readlines():
        line = line.strip()
        # find all non-dots
        for m in re.finditer(r"[^\.]", line):
            splitter_loc = m.start()
            if splitter_loc in tachyon_beams:
                tachyon_beams.remove(splitter_loc)
                tachyon_beams.update((splitter_loc-1, splitter_loc+1))
                split_count += 1
            
            # 'S' is the start
            if line[splitter_loc] == 'S':
                print('starting')
                tachyon_beams.add(splitter_loc)
            print(splitter_loc)
        print(line, tachyon_beams)

print()
print('split count:',split_count)
