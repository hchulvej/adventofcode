# We load the data file
with open("2025_01.txt") as f:
    lines = f.read().splitlines()

def change_rotation(rotation):
    if rotation[0] == "L":
        temp = int(rotation[1:])
        full_rounds = 0
        while temp >= 100:
            full_rounds += 1
            temp -= 100
        temp = 100 - temp
        return "R" + str(temp + full_rounds * 100)
    return rotation

def move_dial(dial, rotation):
    rotation = change_rotation(rotation)
    rot = int(rotation[1:])
    return (dial + rot) % 100

## Part 1
starting_dial = 50
number_of_zeros = 0
for line in lines:
    starting_dial = move_dial(starting_dial, line)
    if starting_dial == 0:
        number_of_zeros += 1

print("Password:", number_of_zeros)

## Part 2
number_of_zeros = 0
position = 50
for line in lines:
    no_of_moves = int(line[1:])
    direction = line[0]
    for _ in range(no_of_moves):
        if direction == "R":
            position = (position + 1) % 100
        else:
            position = (position - 1) % 100
        if position == 0:
            number_of_zeros += 1
    

print("Total number of zeroes:",  number_of_zeros)
