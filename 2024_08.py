import numpy as np
from itertools import combinations

def read_input(input_file):
    with open(input_file) as f:
        lines = [list(line.strip()) for line in f.readlines()]
    return lines

raw_input = read_input("2024_08_1.txt")
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

memo = dict()

def squared_difference(coordinate_difference):
    x, y = coordinate_difference
    if (x, y) in memo:
        return memo[(x, y)]
    if (x < 0 or y < 0):
        return squared_difference((abs(x), abs(y)))
    else:
        memo[(x, y)] = x**2 + y**2
        return memo[(x, y)]

def are_in_line(ant1, ant2, point):
    v1, v2 = (ant2[0] - ant1[0], ant2[1] - ant1[1])
    w1, w2 = (point[0] - ant1[0], point[1] - ant1[1])
    return v1 * w2 - v2 * w1 == 0



def antinodes_part_one(antennas):
    antinodes = set()
    for row in range(len(data)):
        for col in range(len(data[0])):
            for antenna_name in antennas:
                for ant1, ant2 in combinations(antennas[antenna_name], 2):
                    dist1 = squared_difference((ant1[0] - col, ant1[1] - row))
                    dist2 = squared_difference((ant2[0] - col, ant2[1] - row))
                    if (dist1 == 4 * dist2 or dist2 == 4 * dist1) and are_in_line(ant1, ant2, (col, row)):
                        antinodes.add((col, row))
    return antinodes

print(len(antinodes_part_one(antennas)))


# Part Two

def antinodes_part_two(antennas):
    antinodes = set()
    for row in range(len(data)):
        for col in range(len(data[0])):
            for antenna_name in antennas:
                for ant1, ant2 in combinations(antennas[antenna_name], 2):
                    if are_in_line(ant1, ant2, (col, row)):
                        antinodes.add((col, row))
    return antinodes

print(len(antinodes_part_two(antennas)))