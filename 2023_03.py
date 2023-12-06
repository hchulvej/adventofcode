input = []

with open('2023_03_1.txt', 'r') as f:
    for l in f.readlines():
        input.append(l.replace('\n', ''))


nr = len(input)
nc = len(input[0])

print("Number of rows: " + str(nr))
print("Number of columns: " + str(nc))

def get_value(t):
    return input[t[0]][t[1]]

def adjacent_coordinates(r, c):
    circle = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    return [(r + dr, c + dc) for dr, dc in circle if 0 <= r + dr < nr and 0 <= c + dc < nc]

def valid_number(r, c):
    return get_value((r, c)).isdigit() and len([get_value(t) for t in adjacent_coordinates(r,c) if not get_value(t).isdigit() and get_value(t) != '.']) > 0

valid_numbers = []

for r in range(nr):
    number = ""
    counts = False
    for c in range(nc):
        if get_value((r, c)).isdigit():
            number += get_value((r, c))
            if valid_number(r, c):
                counts = True
            if c == 139 and counts:
                valid_numbers.append(int(number))
        else:
            if (len(number) > 0) and counts:
                valid_numbers.append(int(number))
            counts = False
            number = ""

print(sum(valid_numbers))
