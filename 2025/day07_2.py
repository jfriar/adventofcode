#!/usr/bin/env python3

import re

input_file = 'day07_input.txt'
#input_file = 'day07_sample.txt'

particle_paths = {}
line_num = 0
with open(input_file) as f:
    for line in f.readlines():
        line = line.strip()
        new_paths = {}
        # find all non-dots
        for m in re.finditer(r"[^\.]", line):
            splitter_loc = m.start()
            if splitter_loc in particle_paths.keys():
                num_particles = particle_paths.pop(splitter_loc)
                particle_paths[splitter_loc-1] = particle_paths.get(splitter_loc-1, 0) + num_particles
                particle_paths[splitter_loc+1] = particle_paths.get(splitter_loc+1, 0) + num_particles

            # 'S' is the start
            if line[splitter_loc] == 'S':
                print('starting')
                particle_paths[splitter_loc] = 1
        print('line_num', line_num)
        line_num += 1

print()
print('number of particle_paths:', sum(particle_paths.values()))
