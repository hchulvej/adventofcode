input = []

with open('2023_03_1.txt', 'r') as f:
    for l in f.readlines():
        input.append(l.replace('\n', ''))


nr = len(input)
nc = len(input[0])

print("Number of rows: " + str(nr))
print("Number of columns: " + str(nc))

numbers = []
symbols = []

for r, row in enumerate(input):
    for c, col in enumerate(row):
        if input[r][c] == '.':
            continue
        elif input[r][c].isdigit():
            num = str(input[r][c])
            inc = 1
            while c + inc < nc and input[r][c + inc].isdigit():
                num += str(input[r][c + inc])
                inc += 1
            if (c > 0 and not input[r][c-1].isdigit()) or c == 0:
                numbers.append((int(num), r, c, c + inc - 1))
        else:
            symbols.append((input[r][c],(r,c)))

part1 = 0
part2 = 0

for symbol, pos in symbols:
    prod = 1
    count = 0
    for num in [n for n in numbers if n[1] in [pos[0] - 1, pos[0], pos[0] + 1] and pos[1] >= n[2] - 1 and pos[1] <= n[3] + 1]:
        part1 += int(num[0])
        if symbol == "*":
            prod *= int(num[0])
            count += 1
    if count == 2:
        part2 += prod
            
        

print("Part 1: " + str(part1))
print("Part 2: " + str(part2))