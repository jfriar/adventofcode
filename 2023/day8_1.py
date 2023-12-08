#!/usr/bin/env python3
import re

input_file = 'day8_input.txt'
#input_file = 'day8_test.txt'
#input_file = 'day8_test2.txt'


def lookup_next_node(node, instruction):
    # element = (xxx, yyy)
    i = 0 if instruction == 'L' else 1
    return node[i]


with open(input_file) as f:
    data = [x.strip() for x in f.readlines()]
    instructions = data.pop(0)
    blank_line = data.pop(0)
    nodes = {}
    for line in data:
        node, l, r = re.findall(r"[A-Z]+", line)
        nodes[node] = (l, r)

track_elements = []
element = 'AAA'
while element != 'ZZZ':
    for instruction in instructions:
        element = lookup_next_node(nodes[element], instruction)
        track_elements.append(element)

print(len(track_elements))
print('correct:', 18157)
