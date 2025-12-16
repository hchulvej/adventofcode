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


def count_paths_efficiently():
    """
    Sparse DP: counts paths from 'S' (row 0) to last row.
    Time: O(sum_reachable_per_row * 3) ~ O(total_reached_states)
    Space: O(reachable columns in a row)
    """

    # Starting column
    start_c = data[0].find("S")
    if start_c == -1:
        return 0

    # Optional: precompute passable columns per row for faster membership
    # visited is assumed to be a set of (r, c)
    passable_cols = [set() for _ in range(rows)]
    for (r, c) in visited:
        if 0 <= r < rows:
            passable_cols[r].add(c)

    prev = {start_c: 1}

    for r in range(rows - 1):
        row_next = data[r + 1]
        next_ = defaultdict(int)

        # Only iterate reached columns
        for c_prev, ways in prev.items():
            if ways == 0:
                continue

            # Try three moves
            for move in (-1, 0, 1):
                c_next = c_prev + move
                if not (0 <= c_next < cols):
                    continue

                # Check passable
                if c_next not in passable_cols[r + 1]:
                    continue

                # Movement rules
                if move == 0:
                    # Straight always allowed
                    next_[c_next] += ways
                else:
                    # Diagonal allowed only if character at (r+1, c_prev) is '^'
                    if 0 <= c_prev < cols and row_next[c_prev] == "^":
                        next_[c_next] += ways

        prev = next_

    return sum(prev.values())

print("Part 2: The number of distinct paths to the last row is", count_paths_efficiently())