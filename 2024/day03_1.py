#!/usr/bin/env python3
import re

input_file = 'day03_input.txt'
# input_file = 'day03_sample.txt'


def mul(x,y):
    return x*y

with open(input_file) as f:
    sum_mul = 0
    for line in f.readlines():
        statements = re.findall(r'mul\(\d+,\d+\)', line)
        for s in statements:
            sum_mul += eval(s)
    print(sum_mul)
