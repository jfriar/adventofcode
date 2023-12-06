#!/usr/bin/env python3
import re

input_file = 'day6_input.txt'


def parse_input(data):
    race_times = []
    max_dist = []
    for line in data:
        if line.startswith('Time:'):
            race_times = [int(d) for d in re.findall(r"\d+", line)]
        elif line.startswith('Distance:'):
            max_dist = [int(d) for d in re.findall(r"\d+", line)]
    return race_times, max_dist


def margin_of_error(race_time, distance):
    set_speed_for_win = []
    for _race_time in range(race_time):
        speed = race_time - _race_time
        _distance = _race_time * speed
        if _distance > distance:
            set_speed_for_win.append(speed)
    # print(set_speed_for_win)
    return len(set_speed_for_win)


with open(input_file) as f:
    data = [x.strip() for x in f.readlines()]

race_times, max_dist = parse_input(data)

solve = []
for i, race_time in enumerate(race_times):
    moe = margin_of_error(race_time, max_dist[i])
    solve.append(moe)

result = 1
for i in solve:
    result *= i
print(result)
print('should be: 505494')
