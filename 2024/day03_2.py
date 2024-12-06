#!/usr/bin/env python3
import re

input_file = 'day03_input.txt'
# input_file = 'day03_sample2.txt'


def mul(x,y):
    return x*y

with open(input_file) as f:
    sum_mul = 0
    enabled = True
    for line in f.readlines():
        statements = re.findall(r'''mul\(\d+,\d+\)|do\(\)|don't\(\)''', line)
        for s in statements:
            # print(s)
            if s == 'do()':
                enabled = True
            elif s == "don't()":
                enabled = False
            elif enabled:
                sum_mul += eval(s)
    print(sum_mul)
