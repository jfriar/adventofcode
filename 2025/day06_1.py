#!/usr/bin/env python3

import math

input_file = 'day06_input.txt'
#input_file = 'day06_sample.txt'

problems = []
with open(input_file) as f:
    for line in f.readlines():
        line = line.strip()
        for i, val in enumerate(line.split()):
            if val == '*':
                problems[i] = math.prod(problems[i])
            elif val == '+':
                problems[i] = sum(problems[i])
            else:
                if i < len(problems):
                    problems[i].append(int(val))
                else:
                    problems.append([int(val)])
#print(problems)
print(sum(problems))
