from itertools import combinations

input = open("2023_11_1.in").read().splitlines()

# Finding empty rows and columns
empty_rows = [r for r in range(len(input)) if input[r].count("#") == 0]
empty_cols = [c for c in range(len(input[0])) if not "#" in [input[r][c] for r in range(len(input))]]

galaxies = []

for r in range(len(input)):
    for c in range(len(input[r])):
        if input[r][c] == "#":
            galaxies.append((r,c))

def manhattan(gal_1, gal_2, factor):
    r1, c1 = gal_1 
    r2, c2 = gal_2
    empty_rows_between = len([r for r in empty_rows if min(r1, r2) < r < max(r1, r2)])
    empty_cols_between = len([c for c in empty_cols if min(c1, c2) < c < max(c1, c2)])
    return abs(r1 - r2) + abs(c1 - c2) + factor * (empty_rows_between + empty_cols_between)

# Part 1
git = combinations(galaxies,2)
total = 0
for c in git:
    total += manhattan(c[0], c[1], 1)

print("Part 1: Total distance is", total)

# Part 2
git = combinations(galaxies,2)
total = 0
for c in git:
    total += manhattan(c[0], c[1], 999999)

print("Part 2: Total distance is", total)



