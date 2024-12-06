#!/usr/bin/env python3

input_file = 'day02_input.txt'
# input_file = 'day02_sample.txt'


def check_safe(report):
    direction = 'increasing' if report[0] < report[1] else 'decreasing'
    is_safe = True
    for i, level in enumerate(report):
        if i+1 == len(report):
            # we have reached the end
            break
        next_level = report[i+1]
        difference = abs(next_level - level)
        if difference > 3 or difference < 1:
            is_safe = False
            break
        if direction == 'increasing':
            if level >= next_level:
                is_safe = False
                break
        else:
            if level <= next_level:
                is_safe = False
                break

    return is_safe


with open(input_file) as f:
    safe_count = 0
    for line in f.readlines():
        report = [int(level) for level in line.split()]
        is_safe = check_safe(report)
        if is_safe:
            safe_count += 1
            print(line.rstrip(), " safe")
        else:
            for i in range(0, len(report)):
                report_copy = report.copy()
                del report_copy[i]
                is_safe = check_safe(report_copy)
                if is_safe:
                    safe_count += 1
                    print(line.rstrip(), " safe")
                    break
            if not is_safe:
                print(line.rstrip(), " not safe")
    print('\nsafe count:', safe_count)


