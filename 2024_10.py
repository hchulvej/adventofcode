import numpy as np
from collections import deque

def read_input(input_file):
    with open(input_file) as f:
        lines = [list(map(int, list(line.strip()))) for line in f.readlines()]
    return lines

raw_input = read_input("2024_10_1.txt")

map = np.array(raw_input)

# Part One

trailheads = list(zip(np.where(map == 0)[0], np.where(map == 0)[1]))

trails = {th : dict() for th in trailheads}
directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def on_map(point):
    x, y = point
    return 0 <= x < map.shape[0] and 0 <= y < map.shape[1]

for th in trailheads:
    trails[th][0] = [th]
    for i in range(1, 10):
        trails[th][i] = []
    
def add_to_trail(trailhead, level):
    for th in trails[trailhead][level - 1]:
        x, y = th
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if on_map((nx, ny)) and map[nx, ny] == level and (nx, ny) not in trails[trailhead][level]:
                trails[trailhead][level].append((nx, ny))
    return


for th in trailheads:
    for level in range(1, 10):
        add_to_trail(th, level)

def score(trailhead):
    return len(trails[trailhead][9])

scores = [score(th) for th in trailheads]

print(sum(scores))