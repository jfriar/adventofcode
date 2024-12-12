#!/usr/bin/env python3

input_file = 'day07_input.txt'
# input_file = 'day07_sample.txt'


def solve(equation):
    answer, components = equation.split(': ')
    answer = int(answer)
    # components = [int(c) for c in components.split()]
    components = components.split(' ')
    solutions = [components[0]]
    for c in components[1:]:
        new_solutions = []
        for s in solutions:
            new_solutions.append(s+' + '+c)
            new_solutions.append(s+' * '+c)
        solutions = new_solutions
    # print(components, solutions)
    operator = None
    calibration_result = None
    for s in solutions:
        s_answer = 0
        for val in s.split(' '):
            if val in ('*', '+'):
                operator = val
            else:
                val = int(val)
                if operator == '*':
                    s_answer *= val
                    operator = None
                elif operator == '+':
                    s_answer += val
                    operator = None
                elif operator is None and s_answer == 0:
                    s_answer = val
                else:
                    raise ValueError('invalid operator')
        # print(answer, s_answer, s)
        if s_answer == answer:
            calibration_result = (answer, s)
            print('answer found:', answer, ':', s)
            return True

    return False


with open(input_file) as f:
    calibration_equations = [line.rstrip() for line in f.readlines()]

total_calibration_results = 0
for ce in calibration_equations:
    if solve(ce):
        total_calibration_results += int(ce.split(':')[0])

print('total_calibration_results:', total_calibration_results)

