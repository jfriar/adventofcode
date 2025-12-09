#!/usr/bin/env python3

import math

input_file = 'day06_input.txt'
#input_file = 'day06_sample.txt'

raw = []
max_len = 0
problems = []
problem_num = 0
with open(input_file) as f:
    for line in f.readlines():
        line = line.strip('\n')
        line_len = len(line)
        if line_len > max_len:
            max_len = line_len
        raw.append(line)

problem = []
problem_action = ''
for col in range(0, max_len):
    col_data = []
    for row in range(0, len(raw)):
        if raw[row][col] in ('*', '+'):
            problem_action = raw[row][col]
        elif raw[row][col] == ' ':
            continue
        else:
            col_data.append(raw[row][col])
    if col_data:
        col_data = int(''.join(col_data))
        problem.append(col_data)

    # either end of the row, or next problem
    if col == max_len - 1 or not col_data:
        # print(problem)
        if problem_action == '*':
            problems.append(math.prod(problem))
        elif problem_action == '+':
            problems.append(sum(problem))
        problem = []
        problem_action = ''

print(sum(problems))

