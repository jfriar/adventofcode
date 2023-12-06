#!/usr/bin/env python3
import re

input_file = 'day6_input.txt'


def parse_input(data):
    for line in data:
        if line.startswith('Time:'):
            race_time = int(''.join([d for d in re.findall(r"\d+", line)]))
        elif line.startswith('Distance:'):
            max_dist = int(''.join([d for d in re.findall(r"\d+", line)]))
    return race_time, max_dist


def margin_of_error(race_time, distance):
    set_speed_for_win = []
    for s in range(race_time):
        r = race_time - s
        _d = s * r
        if _d > distance:
            set_speed_for_win.append(s)
    # print(set_speed_for_win)
    return len(set_speed_for_win)


with open(input_file) as f:
    data = [x.strip() for x in f.readlines()]

print(parse_input(data))
race_time, max_dist = parse_input(data)
moe = margin_of_error(race_time, max_dist)
print(moe)
