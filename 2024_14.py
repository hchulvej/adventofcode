

def read_input(input_file):
    with open(input_file) as f:
        lines = [line.strip() for line in f.readlines()]
    return lines

raw_input = read_input("2024_14_1.txt")

robots = []
WIDTH = 101
HEIGHT = 103
MID_X = WIDTH // 2
MID_Y = HEIGHT // 2
print(MID_X, MID_Y)

def quadrant(pos):
    x, y = pos
    if x < MID_X and y < MID_Y:
        return 2
    if x > MID_X and y < MID_Y:
        return 1
    if x < MID_X and y > MID_Y:
        return 3
    if x > MID_X and y > MID_Y:
        return 4
    return 0

for line in raw_input:
    line = line.replace("p=", "").replace("v=", "").replace(" ", ",")
    p1, p2, v1, v2 = map(int, line.split(","))
    robots.append({"ip": (p1, p2), "v": (v1, v2), "p": (p1, p2)})

def move(robot, position):
    v1, v2 = robot["v"]
    x, y = position
    return ((x + v1) % WIDTH, (y + v2) % HEIGHT)


# Part One

robot_count = dict({0 : 0, 1 : 0, 2 : 0, 3 : 0, 4 : 0})

for robot in robots:
    for _ in range(100):
        robot["p"] = move(robot, robot["p"])
    robot_count[quadrant(robot["p"])] += 1

print(robot_count[1] * robot_count[2] * robot_count[3] * robot_count[4])

# Part Two

