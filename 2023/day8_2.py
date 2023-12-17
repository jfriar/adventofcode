#!/usr/bin/env python3
import re

input_file = 'day8_input.txt'
#input_file = 'day8_test.txt'
#input_file = 'day8_test2.txt'
#input_file = 'day8_test3.txt'


def gcd(a, b):
    # greatest common divisor
    a, b = (a, b) if a >= b else (b, a)
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def lcm(a, b):
    # least common multiple
    if a == b == 0:
        return 0
    return int(a * (b / gcd(a, b)))


def lcm_multi(a):
    # a is an iterable
    if len(set(a)) == 1:
        return a[0]

    _lcm = a
    while not all(_lcm[i] == _lcm[i+1] for i in range(0, len(_lcm)-1)):
        new_lcm = []
        for i in range(0, len(_lcm)-1):
            new_lcm.append(lcm(_lcm[i], _lcm[i+1]))
        _lcm = new_lcm
    return _lcm[0]


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
        node, l, r = re.findall(r"\w+", line)
        nodes[node] = (l, r)

elements = [k for k in nodes if k.endswith('A')]
print('elements:', elements)
track_elements = []
# find each element's path
for element in elements:
    # print(element)
    _track = []
    while not element.endswith('Z'):
        for instruction in instructions:
            element = lookup_next_node(nodes[element], instruction)
            _track.append(element)
    track_elements.append(len(_track))

# print(gcd(2, 6))
# print(lcm(2, 6))
# print()
# print(lcm_multi([3,4,6]))
print()
print('steps:', lcm_multi(track_elements))
print('correct:', 14299763833181)
