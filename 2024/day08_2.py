#!/usr/bin/env python3
import math

input_file = 'day08_input.txt'
# input_file = 'day08_sample.txt'


def get_slope(x1, y1, x2, y2):
    if x1 == x2 or y1 == y2:
        return float(0)
    return float(abs(y2 - y1) / abs(x2 - x1))


def get_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)


def find_pairs(source_position, other_positions):
    slopes = {}
    for position in other_positions:
        slope = get_slope(*source_position, *position)
        distance = get_distance(*source_position, *position)
        if slope in slopes:
            if distance < get_distance(*source_position, *slopes[slope]):
                slopes[slope] = position
        else:
            slopes[slope] = position
    pairs = set()
    for position in slopes.values():
        if location_to_freq[source_position] == location_to_freq[position]:
            pairs.add(position)
    return pairs


with open(input_file) as f:
    antenna_map = [line.rstrip() for line in f.readlines()]

y_len = len(antenna_map)
x_len = len(antenna_map[0])
frequency = {}
location_to_freq = {}
for y, row in enumerate(antenna_map):
    for x, val in enumerate(row):
        if val == '.':
            continue
        else:
            frequency.setdefault(val, set()).add((x, y))
            location_to_freq[(x, y)] = val

print(location_to_freq)
antenna_pairs = {}
seen = set()
for pos, freq in location_to_freq.items():
    other_locations = list(location_to_freq.keys())
    other_locations.remove(pos)
    # for other_pos in other_locations:
    pairs = find_pairs(pos, other_locations)
    antenna_pairs[pos] =  pairs
    print('freq:', freq, 'pos:', pos, 'pairs:', pairs)
    for pair_pos in pairs:
        if pos < pair_pos:
            _seen = (pos, pair_pos)
        else:
            _seen = (pair_pos, pos)
        seen.add(_seen)

print('antenna_pairs:', antenna_pairs)
print('seen:', seen)

antinodes = set()

for ((x1, y1), (x2, y2)) in seen:
    multiplier = 0
    keep_looping = True
    while keep_looping:
        keep_looping = False
        d_x = abs(x2 - x1) * multiplier
        if x2 < x1:
            a_x1 = x1 + d_x
            a_x2 = x2 - d_x
        else:
            a_x1 = x1 - d_x
            a_x2 = x2 + d_x

        d_y = abs(y2 - y1) * multiplier
        if y2 < y1:
            a_y1 = y1 + d_y
            a_y2 = y2 - d_y
        else:
            a_y1 = y1 - d_y
            a_y2 = y2 + d_y
        multiplier += 1
        
        # stay inbound
        if 0 <= a_x1 < x_len and 0 <= a_y1 < y_len:
            antinodes.add((x1, y1))
            antinodes.add((a_x1, a_y1))
            keep_looping = True
        if 0 <= a_x2 < x_len and 0 <= a_y2 < y_len:
            antinodes.add((x2, y2))
            antinodes.add((a_x2, a_y2))
            keep_looping = True

print(len(antinodes))
# print(antinodes)

