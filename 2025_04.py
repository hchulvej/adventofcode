def read_data():
    with open("2025_04.txt") as f:
        return f.read().split("\n")


data = [list(line) for line in read_data()]

def eight_neigbors(x,y, mx, my):
    neighbors = []
    for dx in [-1,0,1]:
        for dy in [-1,0,1]:
            if dx == 0 and dy == 0:
                continue
            if 0 <= x+dx <= mx and 0 <= y+dy <= my:
                neighbors.append((x+dx, y+dy))
    return neighbors

def check_number_of_rolls(x, y, input_data):
    count = 0
    for nx, ny in eight_neigbors(x, y, len(input_data)-1, len(input_data[0])-1):
        if input_data[nx][ny] == '@':
            count += 1
    return count

## Part 1

def count_rolls(input_data):
    accessible_positions = 0
    for x in range(len(input_data)):
        for y in range(len(input_data[0])):
            if input_data[x][y] == '@':
                rolls = check_number_of_rolls(x, y, input_data)
                if rolls < 4:
                    accessible_positions += 1
    return accessible_positions


print("Part 1: Number of accessible rolls = ", count_rolls(data))

## Part 2

data_part2 = [list(line) for line in read_data()]

# Like Part 1 but moves accessible rolls
def count_rolls_part2(input_data):
    accessible_positions = 0
    for x in range(len(input_data)):
        for y in range(len(input_data[0])):
            if input_data[x][y] == '@':
                rolls = check_number_of_rolls(x, y, input_data)
                if rolls < 4:
                    accessible_positions += 1
                    input_data[x][y] = '.'
    return accessible_positions

def count_all_rolls_part2(input_data):
    total_accessible = 0
    while True:
        accessible = count_rolls_part2(input_data)
        if accessible == 0:
            break
        total_accessible += accessible
    return total_accessible

print("Part 2: Number of accessible rolls = ", count_all_rolls_part2(data_part2))