#!/usr/bin/env python3

input_file = 'day2_input.txt'

limits = {'red': 12,
          'green': 13,
          'blue': 14}

with open(input_file) as f:
    valid_game_ids = []
    for game_data in f.readlines():
        game_data = game_data.rstrip().split(': ')
        game_id = int(game_data[0].split(' ')[1])
        limit_hit = False
        for gd in game_data[1].split('; '):
            for cube in gd.split(', '):
                cube = cube.split(' ')
                if limits[cube[1]] < int(cube[0]):
                    #print('game id:', game_id, 'limit hit. cube:', cube)
                    limit_hit = True
                    break
            if limit_hit:
                break
        if not limit_hit:
            valid_game_ids.append(game_id)
    print(sum(valid_game_ids))
