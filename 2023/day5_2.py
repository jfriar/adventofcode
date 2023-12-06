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


def find_location(start_type, start_val, start_range, map_data, debug=False):
    src_data = map_data[start_type]
    dest_type = src_data['dest']
    dest_val = start_val

    locations = []
    remaining = []
    # for each of the ranges of this start type:
    for src_range in src_data['range']:
        dest_val = None
        dest_range = None
        val_trans = src_range['src'] - src_range['dest']

        # if start_val, start_val+start_range is bigger than the current range
        if start_val < src_range['src'] and src_range['src']+src_range['range'] < start_val+start_range:
            start_val1 = start_val
            start_range1 = src_range['src'] - start_val1
            remaining.append((start_val1, start_range1))

            start_val2 = src_range['src'] + src_range['range']
            start_range2 = start_val + start_range - start_val2 
            remaining.append((start_val2, start_range2))

            dest_val = src_range['src'] - val_trans
            dest_range = src_range['range']
            break

        # if start_val and start_val+start_range are within this range
        elif src_range['src'] <= start_val and start_val+start_range <= src_range['src']+src_range['range']:
            dest_val = start_val - val_trans
            dest_range = start_range
            break

        # if start_val is within range, but range extends to another range
        elif src_range['src'] <= start_val < src_range['src'] + src_range['range']:
            start_val1 = src_range['src'] + src_range['range']
            start_range1 = start_val + start_range - start_val1
            remaining.append((start_val1, start_range1))

            dest_val = start_val - val_trans
            dest_range = src_range['src'] + src_range['range'] - start_val
            break
            
        # if start_val+start_range is within range, but start_val starts before this range
        elif src_range['src'] < start_val+start_range <= src_range['src'] + src_range['range']:
            start_val1 = start_val
            start_range1 = src_range['src'] - start_val1
            remaining.append((start_val1, start_range1))

            dest_val = src_range['dest']
            dest_range = start_val + start_range - start_val
            break

    if len(remaining) > 0:
        for r in remaining:
            locations.append(find_location(start_type, r[0], r[1], map_data, debug))


    if all(i is None for i in [dest_val, dest_range]):
        # print('no translation', start_val, start_range)
        dest_val = start_val
        dest_range = start_range

    if debug:
        print(' - start_type:', start_type, 'start_val:', start_val, '| dest_type:', dest_type, 'dest_val:', dest_val)

    if dest_type == 'location-to':
        if dest_val == 0:
            # I don't know why this worked (ignore the 0 for dest_val only if
            # on a location-to loop)
            dest_val = start_val
            print('warning', start_val, start_range)

        locations.append(dest_val)
        return min(locations)

    locations.append(find_location(dest_type, dest_val, dest_range, map_data, debug))
    return min(locations)


with open(input_file) as f:
    data = [x.strip() for x in f.readlines()]

# from pprint import pprint
# pprint(parse_map_data(data))

maps = parse_map_data(data)

location_vals = []
for i in range(0, len(maps['seeds']), 2):
    seed = maps['seeds'][i]
    seed_range = maps['seeds'][i+1]
    location = find_location('seed-to', seed, seed_range, maps, False)

    location_vals.append(location)
    print('seed:', seed, 'seed_range:', seed_range, 'location:', location)

print('min:', min(location_vals))

