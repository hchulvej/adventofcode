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
        temp_g.append(list(line))

transposed_grids = [grid.transpose() for grid in grids]
       

# Helper functions
def are_equal(np_arr_1, np_arr_2):
    return all(np_arr_1 == np_arr_2)

def is_reflection_line(grid, line_no):
    return all([are_equal(grid[line_no - k], grid[line_no + 1 + k]) for k in range(len(grid)) if line_no - k >= 0 and line_no + 1 + k < len(grid)])

def horizontal_reflection_lines(grid_no):
    grid = grids[grid_no]
    return [r for r in range(len(grid) - 1) if is_reflection_line(grid, r)] 

def vertical_reflection_lines(grid_no):
    grid = transposed_grids[grid_no]
    return [r for r in range(len(grid) - 1) if is_reflection_line(grid, r)]

# Part 1
score_p1 = 0
for i in range(len((grids))):
    score_p1 += sum([100*(r + 1) for r in horizontal_reflection_lines(i)])
    score_p1 += sum([c + 1 for c in vertical_reflection_lines(i)])
print("Part 1:", score_p1)

# Part 2