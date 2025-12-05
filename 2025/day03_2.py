#!/usr/bin/env python3

input_file = 'day03_input.txt'
#input_file = 'day03_sample.txt'

joltages = []
num_batteries = 12
with open(input_file) as f:
    for line in f.readlines():
        line = line.strip()

        # greedy approach using monotonic stack, thanks google search.
        stack = []
        num_batteries = 12
        removals_left = len(line) - num_batteries

        # for each digit, compare it to the previous digit in the stack.
        # if the previous digit is smaller, and more digits can be removed,
        # remove the previous digit and keep checking
        for d in line:
            while stack and stack[-1] < d and removals_left > 0:
                stack.pop()
                removals_left -= 1
            stack.append(d)

        joltage = ''.join(stack[:num_batteries])
        print(line, joltage)
        joltages.append(int(joltage))

print(sum(joltages))
