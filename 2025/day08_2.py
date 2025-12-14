#!/usr/bin/env python3

import math

input_file = 'day08_input.txt'
#input_file = 'day08_sample.txt'

# get all the junction box locations
box_positions = []
with open(input_file) as f:
    for line in f.readlines():
        x, y, z = map(int,line.strip().split(','))
        box_positions.append((x,y,z))

box_count = len(box_positions)
#print(box_positions)

# get all the junction box distances
pos = box_positions.pop(0)
sorted_pos = []
while pos:
    for next_pos in box_positions:
        distance = math.sqrt((next_pos[0] - pos[0])**2 + (next_pos[1] - pos[1])**2 + (next_pos[2] - pos[2])**2)
        # print((distance, pos, next_pos))
        sorted_pos.append((distance, pos, next_pos))
    if box_positions:
        pos = box_positions.pop(0)
    else:
        pos = False

sorted_pos = list(sorted(sorted_pos))

circuits = []
for dist, box_a, box_b in sorted_pos:
    # print('checking:', box_a, box_b)
    found = []
    for circuit in circuits:
        if box_a in circuit and box_b in circuit:
            # print('skipping:', (box_a, box_b))
            continue
        if box_a in circuit or box_b in circuit:
            found.append(circuit)

    len_found = len(found)
    if len_found == 0:
        circuits.append(set([box_a, box_b]))
    else:
        for f in found:
            # print('removing:', f)
            circuits.remove(f)
        circuit_merged = set().union(*found)
        circuit_merged.add(box_a)
        circuit_merged.add(box_b)
        # print('adding:', circuit_merged)
        circuits.append(circuit_merged)
        if len(circuit_merged) == box_count:
            print('all the boxes')
            break
    # print()
    if len(circuits) == 1:
        print('len == 1,',(box_a, box_b))

print(box_a[0] * box_b[0])
