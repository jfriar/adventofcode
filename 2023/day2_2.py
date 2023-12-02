#!/usr/bin/env python3

input_file = 'day2_input.txt'

games = {}

with open(input_file) as f:
    for game_data in f.readlines():
        game_data = game_data.rstrip().split(': ')
        game_id = int(game_data[0].split(' ')[1])
        games[game_id] = {'red': 0,
                          'blue': 0,
                          'green': 0}
        for gd in game_data[1].split('; '):
            for cube in gd.split(', '):
                cube = cube.split(' ')
                if games[game_id][cube[1]] < int(cube[0]):
                    games[game_id][cube[1]] = int(cube[0])

powers = []
for game_id, game_data in games.items():
    val = 1
    for color, num in game_data.items():
        val = val * num
    powers.append(val)
print(sum(powers))
