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
    trails[th][0] = [[th[0], th[1]]]
    for i in range(1, 10):
        trails[th][i] = []
    
def add_to_trail(trailhead, level):
    for th in trails[trailhead][level - 1]:
        x, y = th[-2], th[-1]
        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            if on_map((new_x, new_y)) and map[new_x, new_y] == level:
                new_trail = th + [new_x, new_y]
                trails[trailhead][level].append(new_trail)
    return


for th in trailheads:
    for i in range(1, 10):
        add_to_trail(th, i)


# Part One

reachable_nines = [set() for _ in range(len(trailheads))]

for i, th in enumerate(trailheads):
    for t in trails[th][9]:
        reachable_nines[i].add((t[-2], t[-1]))

print(sum([len(r) for r in reachable_nines]))

# Part Two

print(sum([len(trails[th][9]) for th in trailheads]))