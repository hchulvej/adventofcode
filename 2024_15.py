from collections import deque

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

instructions = list(instructions)       

# Part One

def move_boxes(set_of_boxes, first_box, direction):
    dx, dy = DIRS[direction]
    f_x, f_y = first_box
    m = 0
    while (f_x + m * dx, f_y + m * dy) in set_of_boxes:
        m += 1
    after_boxes = (f_x + m * dx, f_y + m * dy)
    if after_boxes in walls:
        return (set_of_boxes, False)
    else:
        set_of_boxes.remove(first_box)
        set_of_boxes.add(after_boxes)
        return (set_of_boxes, True)
    
    
def move_robot(set_of_boxes, robot, direction):
    dx, dy = DIRS[direction]
    x, y = robot[0]
    after_robot = (x + dx, y + dy)
    if after_robot in walls:
        return (set_of_boxes, robot)
    elif after_robot in set_of_boxes:
        set_of_boxes, success = move_boxes(set_of_boxes, after_robot, direction)
        if success:
            robot[0] = after_robot
            return (set_of_boxes, robot)
        else:
            return (set_of_boxes, robot)
    else:
        robot[0] = after_robot
        return (set_of_boxes, robot)


def draw_warehouse(robot, walls, boxes, part=1):
    if part == 1:
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
    else:
        for y in range(DIM_Y):
            for x in range(0, 2 * DIM_X, 2):
                if (x, y) in walls:
                    print("##", end="")
                elif (x, y) in boxes:
                    print("[]", end="")
                elif (x, y) == robot[0]:
                    print("@.", end="")
                else:
                    print("..", end="")
            print()
        

for instruction in instructions:
    boxes, robot = move_robot(boxes, robot, instruction)

print(sum(b[0] + 100 * b[1] for b in boxes))

# Part Two

walls = set()
boxes = set()
robot = [(0,0)]

for y, line in enumerate(raw_input):
    if line.count("#") > 0:
        for x, char in enumerate(line):
            if char == "#":
                walls |= {(2 * x, y), (2 * x + 1, y)}
            elif char == "O":
                boxes.add((2 * x, y))
            elif char == "@":
                robot[0] = (2 * x, y)



def affected_boxes(set_of_boxes, first_box, direction):
    aff_boxes = set(first_box)
    dx, dy = DIRS[direction]
    f_x, f_y = first_box #Left side coordinates "["
    # Case 1: Horsiontal movement
    if direction in ["<", ">"]:
        m = 0
        while (f_x + 2 * m * dx, f_y + m * dy) in set_of_boxes:
            aff_boxes.add((f_x + 2 * m * dx, f_y + m * dy))
            m += 1
    # Case 2: Vertical movement
    else:
        queue = deque(first_box)
        while len(queue) > 0:
            x, y = queue.pop()
            # []
            # []
            if (x, y + dy) in set_of_boxes:
                aff_boxes.append((x, y + dy))
            # [][]
            #  []
            if (x - 1, y + dy) in set_of_boxes:
                aff_boxes.append((x - 1, y + dy))
            if (x + 1, y + dy) in set_of_boxes:
                aff_boxes.append((x + 1, y + dy))
    return aff_boxes

print(boxes)
print(list(affected_boxes(boxes, (6,3), "v")))
        
        