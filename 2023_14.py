import numpy as np

input = open("2023_14_test.in").read().splitlines()

grid = np.ndarray((len(input), len(input[0])), dtype=np.uint8)

for line in input:
    grid.a