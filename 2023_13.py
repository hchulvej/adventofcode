input = open("2023_13_test.in").read().splitlines()
input.append("")

grids = []

grid = []
for line in input:
    if len(line) > 0:
        grid.append(line)
    else:
        grids.append(grid)
        grid = []

for r in grids[1]:
    print(r)