import numpy as np

def read_input(input_file):
    with open(input_file) as f:
        lines = [list(line.strip()) for line in f.readlines()]
    return lines

raw_input = read_input("2024_08_2.txt")
data = np.array(raw_input, dtype=str)

def log_antenna_positions(input_data):
    antennas = dict()
    for x, row in enumerate(input_data):
        for y, entry in enumerate(row):
            if entry == '.':
                continue
            if entry in antennas:
                antennas[entry].add((x, y))
            else:
                antennas[entry] = set([(x, y)])
    return antennas

# Part One

antennas = log_antenna_positions(data)

def squared_distance(pos1, pos2):
    return (pos1[0] - pos2[0]) ** 2 + (pos1[1] - pos2[1]) ** 2