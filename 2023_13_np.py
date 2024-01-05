import numpy as np


# Setup
input = open("2023_13_1.in").read().splitlines()
input.append("")

grids = []
temp_g = []

for line in input:
    if len(line) == 0:
        grids.append(np.array(temp_g))
        temp_g = []
    else:
        temp_g.append(list(map(int, line.replace("#","0").replace(".", "1"))))

transposed_grids = [grid.transpose() for grid in grids]
       

# Helper functions
def no_differences(np_arr_1, np_arr_2):
    return np.count_nonzero(np_arr_1 - np_arr_2)

def differences_reflection_line(grid, line_no):
    return sum([no_differences(grid[line_no - k], grid[line_no + 1 + k]) for k in range(len(grid)) if line_no - k >= 0 and line_no + 1 + k < len(grid)])


# Part 1
score_p1 = 0
for grid in grids:
    score_p1 += sum([100 * (r + 1) for r in range(grid.shape[0] - 1) if differences_reflection_line(grid, r) == 0])
for grid in transposed_grids:
    score_p1 += sum([c + 1 for c in range(grid.shape[0] - 1) if differences_reflection_line(grid, c) == 0])
print("Part 1:", score_p1)    

# Part 2
score_p2 = 0
for grid in grids:
    score_p2 += sum([100 * (r + 1) for r in range(grid.shape[0] - 1) if differences_reflection_line(grid, r) == 1])
for grid in transposed_grids:
    score_p2 += sum([c + 1 for c in range(grid.shape[0] - 1) if differences_reflection_line(grid, c) == 1])
print("Part 2:", score_p2)