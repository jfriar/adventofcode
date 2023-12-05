#!/usr/bin/env python3
import collections
import re

input_file = 'day5_input.txt'
#input_file = 'day5_test.txt'


def parse_map_data(data):
    # maps = {'seed-to': {'dest': 'soil', 'range': {src_start: dest_start, src_start+1:dest_start+1, ...}}}
    maps = {}
    map_type = None
    for line in data:
        if line.startswith('seeds: '):
            # seed lines are special
            maps['seeds'] = [int(d) for d in re.findall(r"\d+", line)]
        elif re.match(r"\D+", line):
            # match non-digits
            map_src, map_dest = line.replace(' map:', '').rsplit('-', 1)
            map_dest += '-to'
            maps[map_src] = {'dest': map_dest, 'range': []}
        elif re.match(r"\d+", line):
            # match digits
            dest_start, src_start, map_range = [int(d) for d in re.findall(r"\d+", line)]
            maps[map_src]['range'].append({'src': src_start,
                                           'dest': dest_start,
                                           'range': map_range})
        else:
            map_type = None
    return maps


def find_location(src_type, src_val, map_data, debug=False):
    src_data = map_data[src_type]
    dest_type = src_data['dest']
    dest_val = src_val
    for src_range in src_data['range']:
        if src_range['src'] <= src_val < src_range['src'] + src_range['range']:
            # src_val has a map translation
            val_trans = src_range['src'] - src_range['dest']
            dest_val = src_val - val_trans


    if debug:
        print(' - src_type:', src_type, 'src_val:', src_val, '| dest_type:', dest_type, 'dest_val:', dest_val)
    if dest_type == 'location-to':
        return dest_val
    return find_location(dest_type, dest_val, map_data, debug)


with open(input_file) as f:
    data = [x.strip() for x in f.readlines()]

# from pprint import pprint
# pprint(parse_map_data(data))

maps = parse_map_data(data)

map_type = 'seed-to'
# for seed in [maps['seeds'][1]]:
location_vals = []
for seed in maps['seeds']:
    location = find_location('seed-to', seed, maps)
    location_vals.append(location)
    print('seed:', seed, 'location:', location)

print()
print(min(location_vals))

