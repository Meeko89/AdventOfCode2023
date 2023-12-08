import re

import numpy

files = ["input_data/day2_example1.txt", "input_data/day2.txt"]


if __name__ == '__main__':

    print('\n----- Part One -----')
    limits = {"green": 13, "red": 12, "blue": 14}
    for file in files:
        with open(file, 'r') as f:
            valid_games = []
            for game in f.readlines():
                invalid = False
                parts = game.split(": ")
                id = int(parts[0][5:len(parts[0])])
                handfuls = parts[1].split(";")
                for handful in handfuls:
                    for x in handful.split(", "):
                        color = x.split()[1]
                        nb = int(x.split()[0])
                        if nb > limits[color]:
                            invalid = True
                if not invalid:
                    valid_games.append(id)
            print(file, ": ", sum(valid_games))

    print('\n----- Part Two -----')
    for file in files:
        with open(file, 'r') as f:
            lowest_number = []
            for game in f.readlines():
                game_lowest = {"green": 0, "red": 0, "blue": 0}
                parts = game.split(": ")
                id = int(parts[0][5:len(parts[0])])
                handfuls = parts[1].split(";")
                for handful in handfuls:
                    for x in handful.split(", "):
                        color = x.split()[1]
                        nb = int(x.split()[0])
                        if game_lowest[color] < nb:
                            game_lowest[color] = nb
                lowest_number.append(numpy.prod([nb for nb in game_lowest.values()]))
            print(file, ": ", sum(lowest_number))

