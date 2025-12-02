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
#
# We use the number_of_zeroes from part 1 as a starting point
# In part 2 we count zeroes if
# - we don't land on zero
# - we land on zero but the number of moves is more than 100
# 
def zero_in_positions(dial, rotation):
    rot = int(rotation[1:])
    if move_dial(dial, rotation) == 0:
        if rot < 100:
            return 0
        return rot // 100 - 1
    else:
        return rot // 100
           
        

starting_dial = 50
zeroes_hit = number_of_zeros
for line in lines:
    zeroes_hit += zero_in_positions(starting_dial, line)
    starting_dial = move_dial(starting_dial, line)
print("Zeroes hit:", zeroes_hit)

print(change_rotation("L727"))  # Example usage of change_rotation function
    