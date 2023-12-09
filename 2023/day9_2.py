#!/usr/bin/env python3

input_file = 'day9_input.txt'


with open(input_file) as f:
    data = [list(map(int, x.strip().split(' '))) for x in f.readlines()]

next_history = []
for row in data:
    # print(row)
    row_history = [row]
    while not all(x == 0 for x in row):
        row = [row[i+1] - row[i] for i in range(len(row)-1)]
        row_history.append(row)

    row_history = [list(reversed(r)) for r in row_history]
    for i in range(len(row_history)-1, 0, -1):
        row_history[i-1].append(row_history[i-1][-1] - row_history[i][-1])

    # print(row_history)
    next_history.append((row_history[0][-1]))
    print(row_history[0][-1])
    print()

print('sum:', sum(next_history))
