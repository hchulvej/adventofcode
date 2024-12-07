import numpy as np

def read_input(input_file):
    with open(input_file) as f:
        lines = [list(line.strip()) for line in f.readlines()]
    return lines

raw_input = read_input("2024_06_2.txt")
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

guard = []

boundaries = (0, data.shape[0] - 1, 0,  data.shape[1] - 1)

obstacles = [(x, y) for x, y in zip(np.where(data == '#')[0], np.where(data == '#')[1])]

guard.append(guard_initial_position(data))

def play_one_round(guard, specific_obstacles, boundaries):
    guard_position, guard_direction = guard[-1]
    x, y = guard_position
    if (x < boundaries[0]) or (x > boundaries[1]) or (y < boundaries[2]) or (y > boundaries[3]):
        # Game ends. Guard outside perimeters.
        return "Guard outside perimeters."
    
    match guard_direction:
        case "u":
            guard_position = (x - 1, y)
        case "d":
            guard_position = (x + 1, y)
        case "l":
            guard_position = (x, y - 1)
        case "r":
            guard_position = (x, y + 1)
    
    if guard_position in specific_obstacles:
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

def play_part_one():
    playing = True
    while playing:
        round = play_one_round(guard, obstacles, boundaries)
        if round == "Guard outside perimeters.":
            playing = False
        else:
            guard.append(round)
    return "Game complete."

print(play_part_one())
print(len({p[0] for p in guard})-1)

      
# Part Two




def play_part_two(obs_x, obs_y):
    guard = []
    guard.append(guard_initial_position(data))
    new_obstacles = [o for o in obstacles] + [(obs_x, obs_y)]
    while True:
        round = play_one_round(guard, new_obstacles, boundaries)
        if round == "Guard outside perimeters.":
            return False
        elif round in guard:
            return True
        else:
            guard.append(round)

print([(x, y) for x in range(boundaries[1] + 1) for y in range(boundaries[3] + 1) if play_part_two(x, y)])

print([g for g in guard if (g[0] == (6,4) or g[0] == (6,3))])
               

