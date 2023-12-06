input = []

with open('2023_03_test.txt', 'r') as f:
    for l in f.readlines():
        input.append(l.replace('\n', ''))


nr = len(input)
nc = len(input[0])

print("Number of rows: " + str(nr))
print("Number of columns: " + str(nc))

s = "." +  input[0]
for i in range(1, nr):
    s += input[i]

# 1, 2, ... , nc
# nc + 1, nc + 2, ..., 2nc
def index_to_coords(i):
    return ((i - 1) // nc + 1, (i - 1) % nc + 1)

def coords_to_index(r, c):
    return (r - 1) * nr + c

def adjacent(r, c):
    return [(r + dr, c + dc) for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)] if 0 < r + dr <= nr and 0 < c + dc <= nc]

def is_symbol(i):
    return not (s[i].isdigit() or s[i] == '.')

def counts(i):
    return s[i].isdigit() and any([is_symbol(coords_to_index(*t)) for t in adjacent(*index_to_coords(i))])

total = 0

for r in range(1, nr + 1):
    valid = False
    n = ""
    for c in range(1, nc + 1):
        if not s[coords_to_index(r, c)].isdigit():
            if len(n) > 0 and valid:
                # print(n)
                total = total + int(n)
            valid = False
            n = ""
        else:
            n += s[coords_to_index(r, c)]
            if counts(coords_to_index(r, c)):
                valid = True
    
print("Total: " + str(total))