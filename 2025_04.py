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

def check_number_of_rolls(x, y, data):
    count = 0
    for nx, ny in eight_neigbors(x, y, len(data)-1, len(data[0])-1):
        if data[nx][ny] == '@':
            count += 1
    return count

def count_rolls(data):
    accessible_positions = 0
    for x in range(len(data)):
        for y in range(len(data[0])):
            if data[x][y] == '@':
                rolls = check_number_of_rolls(x, y, data)
                if rolls < 4:
                    accessible_positions += 1
    return accessible_positions


print("Part 1: Number of accessible rolls = ", count_rolls(data))

