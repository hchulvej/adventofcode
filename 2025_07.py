from collections import deque
from collections import defaultdict

def read_data():
    with open("2025_07_test.txt") as f:
        return f.read().split("\n")


## Part 1
data = read_data()

rows = len(data)
cols = len(data[0])

start = (0, data[0].index("S"))

queue = deque([start])
visited = {start}
splitters = set()

while queue:
    r, c = queue.popleft()
    nr = r + 1
    if nr >= rows:
        continue

    ch = data[nr][c]
    if ch == ".":
        if (nr, c) not in visited:
            visited.add((nr, c))
            queue.append((nr, c))
    elif ch == "^":
        splitters.add((nr, c))
        for nc in (c - 1, c + 1):
            if 0 <= nc < cols and (nr, nc) not in visited:
                visited.add((nr, nc))
                queue.append((nr, nc))

print("Part 1: The number of splitters reached is", len(splitters))

## Part 2
# We want to create a function no_of_rows(r,c) that returns the number of rows
# that can be reached from starting position to position (r,c).

visited_per_row = defaultdict(list)

for r, c in visited:
    visited_per_row[r].append((r,c))


paths_of_length = defaultdict(list)
paths_of_length[0] = [[(0, data[0].index("S"))]]

for length in range(1, rows):
    for path in paths_of_length[length - 1]:
        r, c = path[-1]
        if (r + 1, c) in visited:
            new_path = path + [(r + 1, c)]
            paths_of_length[length].append(new_path)
        if (r + 1, c - 1) in visited:
            new_path = path + [(r + 1, c - 1)]
            paths_of_length[length].append(new_path)
        if (r + 1, c + 1) in visited:
            new_path = path + [(r + 1, c + 1)]
            paths_of_length[length].append(new_path)


def path_to_str(path):
    return "".join(f"({r},{c})" for r, c in path)

unique_paths = set()
for path in paths_of_length[rows - 1]:
    unique_paths.add(path_to_str(path))
    
print(len(unique_paths))
