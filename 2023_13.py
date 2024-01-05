input = open("2023_13_1.in").read().splitlines()
input.append("")

grids = []

grid = []
for line in input:
    if len(line) > 0:
        grid.append(line)
    else:
        grids.append(grid)
        grid = []

def check_horizontal(g):
    possible_lines = []
    # Find line no
    # line_i = line_(i+1)
    for i in range(len(g) - 1):
        if g[i] == g[i + 1]:
            possible_lines.append(i)
            
    
    # Check if all rows are reflected
    for i in possible_lines:
        if all([g[i - k] == g[i + 1 + k] for k in range(len(g)) if i - k >=0 and i + 1 + k < len(g)]):
            return 100 * (i + 1)
    
    return 0
    

def check_vertical(g):
    cols = [[g[i][j] for i in range(len(g))] for j in range(len(g[0]))]
    return int(check_horizontal(cols) / 100)


def score(g):
    return check_horizontal(g) + check_vertical(g)
    
        
print("Part 1:", sum([score(g) for g in grids]))