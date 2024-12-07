import numpy as np

def read_input(input_file):
    with open(input_file) as f:
        lines = [list(line.strip()) for line in f.readlines()]
    return lines

raw_input = read_input("2024_06_1.txt")
data = np.array(raw_input, dtype=str)

# Part One

def guard_initial_position(data):
    if np.any(data == '^'):
        return (tuple(zip(np.where(data == '^')[0], np.where(data == '^')[1]))[0], "u")
    if np.any(data == 'v'):
        return (tuple(zip(np.where(data == 'v')[0], np.where(data == '^')[1]))[0], "d")
    if np.any(data == '<'):
        return (tuple(zip(np.where(data == '<')[0], np.where(data == '^')[1]))[0], "l")
    if np.any(data == '>'):
        return (tuple(zip(np.where(data == '>')[0], np.where(data == '^')[1]))[0], "r")

guard = [guard_initial_position(data)]

boundaries = (0, data.shape[0] - 1, 0,  data.shape[1] - 1)

obstacles = [(x, y) for x, y in zip(np.where(data == '#')[0], np.where(data == '#')[1])]

def play_one_round(guard, obstacles, boundaries):
    guard_position, guard_direction = guard[-1]
    x, y = guard_position
    if (x < boundaries[0]) or (x > boundaries[1]) or (y < boundaries[2]) or (y > boundaries[3]):
        # Game ends. Guard outside perimeters.
        return "Guard outside perimeters."
    if guard_direction == "u":
        guard_position = (x - 1, y)
    if guard_direction == "d":
        guard_position = (x + 1, y)
    if guard_direction == "l":
        guard_position = (x, y - 1)
    if guard_direction == "r":
        guard_position = (x, y + 1)
    
    if guard_position in obstacles:
        guard_position = (x, y)
        match guard_direction:
            case "u":
                guard_direction = "r"
            case "r":
                guard_direction = "d"
            case "d":
                guard_direction = "l"
            case "l":
                guard_direction = "u"
    return (guard_position, guard_direction)

def play():
    playing = True
    while playing:
        round = play_one_round(guard, obstacles, boundaries)
        if round == "Guard outside perimeters.":
            playing = False
        else:
            guard.append(round)
    return "Game complete."

print(play())
print(len({p[0] for p in guard})-1)

      
    