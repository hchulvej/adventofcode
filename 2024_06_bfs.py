import numpy as np
from collections import deque

def read_input(input_file):
    with open(input_file) as f:
        lines = [list(line.strip()) for line in f.readlines()]
    return lines

raw_input = read_input("2024_06_1.txt")
data = np.array(raw_input, dtype=str)

# Part One

def guard_initial_position(data):
    for direction, symbol in zip(("u", "d", "l", "r"), ("^", "v", "<", ">")):
        if np.any(data == symbol):
            pos = np.where(data == symbol)
            return (pos[0][0], pos[1][0]), direction

guard = []
boundaries = (0, data.shape[0] - 1, 0,  data.shape[1] - 1)
obstacles = {(x, y) for x, y in zip(*np.where(data == '#'))}
guard.append(guard_initial_position(data))

def play_one_round(guard, obstacles, boundaries):
    guard_position, guard_direction = guard[-1]
    x, y = guard_position
    
    # Check boundaries
    if not (boundaries[0] <= x <= boundaries[1] and boundaries[2] <= y <= boundaries[3]):
        return "Guard outside perimeters."

    # Move the guard
    moves = {"u": (-1, 0), "d": (1, 0), "l": (0, -1), "r": (0, 1)}
    dx, dy = moves[guard_direction]
    new_position = (x + dx, y + dy)
    
    # Obstacle handling
    if new_position in obstacles:
        # Rotate clockwise
        rotations = {"u": "r", "r": "d", "d": "l", "l": "u"}
        guard_direction = rotations[guard_direction]
        return (guard_position, guard_direction)
    return (new_position, guard_direction)

def play_part_one():
    visited_positions = set()
    while True:
        result = play_one_round(guard, obstacles, boundaries)
        if result == "Guard outside perimeters.":
            break
        guard.append(result)
        visited_positions.add(result[0])
    return len(visited_positions)

print("Part One:", play_part_one())

# Part Two

def bfs_reachable_positions():
    """Find all positions reachable by the guard without additional obstacles."""
    start_pos, _ = guard_initial_position(data)
    queue = deque([start_pos])
    visited = set([start_pos])

    while queue:
        x, y = queue.popleft()
        # Check all possible moves
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:  # Up, Down, Left, Right
            nx, ny = x + dx, y + dy
            if (boundaries[0] <= nx <= boundaries[1] and 
                boundaries[2] <= ny <= boundaries[3] and 
                (nx, ny) not in obstacles and 
                (nx, ny) not in visited):
                visited.add((nx, ny))
                queue.append((nx, ny))
    return visited

def simulate_guard_cycle(new_obstacle):
    """Simulate the guard movement with an additional obstacle to detect cycles."""
    guard = [guard_initial_position(data)]
    visited_states = set()

    # Add the new obstacle
    obstacles_with_new = obstacles | {new_obstacle}

    while True:
        state = guard[-1]
        if state in visited_states:
            return True  # Cycle detected
        visited_states.add(state)

        result = play_one_round(guard, obstacles_with_new, boundaries)
        if result == "Guard outside perimeters.":
            return False  # Guard exited the boundary
        guard.append(result)

def play_part_two_optimized():
    reachable_positions = bfs_reachable_positions()
    cycle_positions = 0

    # Test each reachable position as a new obstacle
    for pos in reachable_positions:
        if pos not in obstacles:  # Only test empty spaces
            if simulate_guard_cycle(pos):
                cycle_positions += 1

    return cycle_positions

print("Part Two:", play_part_two_optimized())

