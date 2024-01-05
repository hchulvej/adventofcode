input = open("2023_13_1.in").read().splitlines()
input.append("")

grids = []
temp_g = []

for line in input:
    if len(line) == 0:
        grids.append(tuple(temp_g))
        temp_g = []
    else:
        temp_g.append(tuple(line))

def no_rows(grid):
    return len(grid)

def no_cols(grid):
    return len(grid[0])

def cols(grid):
    return tuple([tuple([grid[r][c] for r in range(no_rows(grid))]) for c in range(no_cols(grid))])

def are_equal(arr_1, arr_2):
    if len(arr_1) != len(arr_2):
        return False
    for i, e in enumerate(arr_1):
        if e != arr_2[i]:
            return False
    return True

def is_reflection_line(grid, line_no):
    return all([are_equal(grid[line_no - k], grid[line_no + 1 + k]) for k in range(no_rows(grid)) if line_no - k >= 0 and line_no + 1 + k < no_rows(grid)])

# Part 1
score_p1 = 0
for grid in grids:
    for r in [r for r in range(no_rows(grid) - 1) if is_reflection_line(grid, r)]:
        score_p1 += 100 * (r + 1)
    cols_grid = cols(grid)
    for c in [c for c in range(no_cols(grid) - 1) if is_reflection_line(cols_grid, c)]:
        score_p1 += c + 1
print("Part 1:", score_p1)

# Part 2

