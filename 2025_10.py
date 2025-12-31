import re, itertools


## Part 1 ##
## Source: https://www.youtube.com/watch?v=OJ4dxrIfDfs

def read_data():
    with open("2025_10.txt") as f:
        target_groups, button_groups = [], []
        for l in f.read().split("\n"):
            match = re.match(r"^\[([.#]+)\] ([()\d, ]+) \{([\d,]+)\}$", l.strip())
            target, buttons, _ = match.groups()
            target = { i for i, c in enumerate(target) if c == "#" }
            buttons = [set(map(int, button[1:-1].split(","))) for button in buttons.split(" ")]
            target_groups.append(target)
            button_groups.append(buttons)
        return target_groups, button_groups

data = read_data()
button_groups = data[1]
taget_groups = data[0]



def solve(target, buttons):
    total = 0
    for count in range(1, len(buttons) + 1):
        for attempt in itertools.combinations(buttons, r=count):
            lights = set()
            for button in attempt:
                lights ^= button # {a, b, c} XOR {b, c, d} = {a, d} - ^= is XOR
            if lights == target:
                total += count
                break
        else:
            continue
        break
    
    return total
                
def solve_all(target_groups, button_groups):
    results = []
    for target, buttons in zip(target_groups, button_groups):
        results.append(solve(target, buttons))
    return results

print("Part 1: ", sum(solve_all(taget_groups, button_groups)))

