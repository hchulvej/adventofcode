from collections import deque
from collections import defaultdict

def read_data():
    with open("2025_07.txt") as f:
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
visited_points = {r : set() for r in range(rows)}
for vp in visited:
    visited_points[vp[0]].add((vp[0], vp[1]))    

ways_prev = defaultdict(int)
ways_prev[start] = 1

for r in range(1, rows):
    ways_cur = defaultdict(int)
    for (_, c) in visited_points[r]:
        ways_cur[c] = ways_prev[c-1] + ways_prev[c] + ways_prev[c+1]
    ways_prev = ways_cur

no_of_paths = sum(ways_prev.values())  # all endpoints in last row

print("Part 2: The total number of paths to the bottom is", no_of_paths)