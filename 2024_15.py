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

first_line = raw_input[0]
DIM_Y = 1
for line in raw_input[1:]:
    if line == first_line:
        break
    DIM_Y += 1

DIM_X = 2 * len(first_line)
the_map = [["." for _ in range(DIM_X)] for _ in range(DIM_Y)]

for y, line in enumerate(raw_input[:DIM_Y]):
    for x, char in enumerate(line):
        if char == "#":
            the_map[y][2 * x] = "#"
            the_map[y][2 * x + 1] = "#"
        elif char == "O":
            the_map[y][2 * x] = "["
            the_map[y][2 * x + 1] = "]"
        elif char == "@":
            the_map[y][2 * x] = "@"
            the_map[y][2 * x + 1] = "."

def can_push_box(left_box, direction):
    lx, ly = left_box
    rx, ry = left_box[0] + 1, left_box[1]
    
    return True

def push_box(left_box, direction):
    dx, dy = DIRS[direction]
    lx, ly = left_box
    rx, ry = left_box[0] + dx, left_box[1] + dy
    if can_push_box(left_box, direction):
        the_map[ly][lx] = "."
        the_map[ry][rx] = "."
        the_map[ly + dy][lx + dx] = "["
        the_map[ry + dy][rx + dx] = "]"
    return True
    

def push_boxes(left_box, direction):
    dx, dy = DIRS[direction]
    lx, ly = left_box
    if dy == 0:
        # Horizontal push
        queue = [[lx, ly]]
        c = 1
        while the_map[ly][lx + c * 2 * dx] == "[": 
            queue.append([(lx + c * 2 * dx, ly)])
            c += 1
        last_box_left = queue[-1]
        if can_push_box(last_box_left, direction):
            while len(queue) > 0:
                box = queue.pop()
                push_box(box, direction)
    else:
        # Vertical push
        affected_boxes = [[lx, ly]]
        queue = [[lx, ly]]
        c = 1
        while len(queue) > 0:
            lx, ly = queue.pop()
            if the_map[ly + c * dy][lx] == "[":
                affected_boxes.append([lx, ly + c * dy])
                queue.append([(lx, ly + c * dy)])
                c += 1
            if the_map[ly + c * dy][lx] == "]":
                affected_boxes.append([lx - 1, ly + c * dy])
                affected_boxes.append([lx + 1, ly + c * dy])
                queue.append([(lx - 1, ly + c * dy)])
                queue.append([(lx + 1, ly + c * dy)])
                c += 1
        if all(can_push_box(box, direction) for box in affected_boxes):
            if direction == "^":
                affected_boxes.sort(key=lambda x: x[1], reverse=True)
            else:
                affected_boxes.sort(key=lambda x: x[1])
            while len(affected_boxes) > 0:
                box = affected_boxes.pop()
                push_box(box, direction)
            
        
            
    

def draw_map_part_2(a_map):
    for y in range(DIM_Y):
        print("".join(a_map[y]))





print(draw_map_part_2(the_map))
print(can_push_box((16,1), "<"))
        
        