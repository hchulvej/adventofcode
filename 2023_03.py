import numpy as np

input = []

with open('2023_03_test.txt', 'r') as f:
    for l in f.readlines():
        input.append(l.replace('\n', ''))

grid = np.array([list(x) for x in input])

print(grid[0][0])