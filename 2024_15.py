def read_input(input_file):
    with open(input_file) as f:
        lines = [line.strip() for line in f.readlines()]
    return lines

raw_input = read_input("2024_15_2.txt")

# Part One

DIM_X, DIM_Y = len(raw_input[0]), len(raw_input)

walls = set()
boxes = set()
robot = [(0,0)]

instructions = ""

DIRS = {"^": (0, -1), "v": (0, 1), "<": (-1, 0), ">": (1, 0)}

for y, line in enumerate(raw_input):
    if line.count("#") > 0:
        for x, char in enumerate(line):
            if char == "#":
                walls.add((x, y))
            elif char == "O":
                boxes.add((x, y))
            elif char == "@":
                robot[0] = (x, y)
    elif len(line) == 0:
        continue
    elif line.count("#") == 0:
        instructions += line       

def push_boxes(box, direction, all_boxes):
    ray = [box]
    x, y = box
    dx, dy = DIRS[direction]
    for step in range(1, max(DIM_X, DIM_Y)):
        nx, ny = x + dx * step, y + dy * step
        if (nx, ny) in all_boxes:
            ray.append((nx, ny))
        else:
            break
    if (nx + dx, ny + dy) in walls:
        return (all_boxes, False)
    else:
        for box in list(ray):
            all_boxes.remove(box)
            all_boxes.add((box[0] + dx, box[1] + dy))
    return (all_boxes, True)

def move(robot, direction, all_boxes):
    x, y = robot[0]
    dx, dy = DIRS[direction]
    nx, ny = x + dx, y + dy
    if (nx, ny) in walls:
        return [(x,y), all_boxes]
    if (nx, ny) in boxes:
        all_boxes, moved = push_boxes((nx, ny), direction, all_boxes)
        if not moved:
            return [(x, y), all_boxes]
    return [(nx, ny), all_boxes]



def draw_warehouse(robot, walls, boxes):
    for y in range(DIM_Y):
        for x in range(DIM_X):
            if (x, y) in walls:
                print("#", end="")
            elif (x, y) in boxes:
                print("O", end="")
            elif (x, y) == robot[0]:
                print("@", end="")
            else:
                print(".", end="")
        print()
        
draw_warehouse(robot, walls, boxes)
for instruction in instructions:
    robot[0], boxes = move(robot, instruction, boxes)
    print(f"Move: {instruction}, Robot: {robot[0]}")
    draw_warehouse(robot, walls, boxes)
    print()