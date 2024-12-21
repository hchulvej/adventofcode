from unionfind import unionfind

def read_input(input_file):
    with open(input_file) as f:
        lines = [list(line.strip()) for line in f.readlines()]
    return lines

raw_input = read_input("2024_12_1.txt")

dim_y, dim_x = len(raw_input), len(raw_input[0])


# Row number is id / dim_x
# Column number is id % dim_x
id_to_coordinates = dict()

for y, row in enumerate(raw_input):
    for x, c in enumerate(row):
        id_to_coordinates[y * dim_x + x] = (x, y)

uf = unionfind(dim_x * dim_y)

for id in range(dim_x * dim_y):
    x, y = id_to_coordinates[id]
    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < dim_x and 0 <= ny < dim_y:
            if not uf.issame(id, dim_x * ny + nx) and raw_input[x][y] == raw_input[nx][ny]:
                uf.unite(id, dim_x * ny + nx)

regions = [[id_to_coordinates[id] for id in group] for group in uf.groups()]


# Part One

def price_part_one(region):
    area = len(region)
    perimeter = 0
    for cell in region:
        x, y = cell
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if (nx, ny) not in region:
                 perimeter += 1
    return area * perimeter                     


print(sum(price_part_one(region) for region in regions))


# Part Two

def price_part_two(region):
    area = len(region)
    perimeter = 0
    for cell in region:
        row, col = cell
        NORTH, SOUTH, EAST, WEST = (row - 1, col), (row + 1, col), (row, col + 1), (row, col - 1)
        NORTH_WEST, NORTH_EAST, SOUTH_WEST, SOUTH_EAST = (row - 1, col - 1), (row - 1, col + 1), (row + 1, col - 1), (row + 1, col + 1)
        # Øverste kant er en ny kant
        if NORTH not in region:
            # Der er en kant øverst
            if (WEST not in region) or (NORTH_WEST in region):
                # Det er en ny kant
                perimeter += 1
        # Venstre kant er en ny kant
        if WEST not in region:
            # Der er en kant venstre
            if (NORTH not in region) or (NORTH_WEST in region):
                # Det er en ny kant
                perimeter += 1
        # Nederste kant er en ny kant
        if SOUTH not in region:
            # Der er en kant nederst
            if (WEST not in region) or (SOUTH_WEST in region):
                # Det er en ny kant
                perimeter += 1
        # Højre kant er en ny kant
        if EAST not in region:
            # Der er en kant højre
            if (SOUTH not in region) or (SOUTH_EAST in region):
                # Det er en ny kant
                perimeter += 1
    return area * perimeter


print(sum(price_part_two(region) for region in regions))