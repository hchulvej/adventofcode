def read_input(input_file):
    with open(input_file) as f:
        lines = [list(line.strip()) for line in f.readlines()]
    return lines

raw_input = read_input("2024_09_1.txt")

data = list(map(int, raw_input[0]))

# Part One

def populate_file_system(data):
    file_system = []
    
    current_index = 0
    for i, val in enumerate(data):
        if i % 2 == 0:
            file_system += [str(current_index)] * val
            current_index += 1
        else:
            file_system += ["."] * val
    return file_system


def compact_file_system(file_system, part=1):
    if part == 1:
        left_index = 0
        right_index = len(file_system) - 1
        while left_index < right_index:
            while file_system[left_index] != ".":
                left_index += 1
            while file_system[right_index] == ".":
                right_index -= 1
            if left_index < right_index:
                tmp = file_system[right_index]
                file_system[right_index] = "."
                file_system[left_index] = tmp
        return file_system
    else:
        return file_system
                    

def score(file_system):
    compacted_file = compact_file_system(file_system)
    eof = compacted_file.index(".")
    checksum = 0
    for i in range(eof):
        checksum += int(compacted_file[i]) * i
    return checksum
        
print(f"Score part one: {score(populate_file_system(data))}")    


# Part Two
## Not my own implementation

file_indices, free_space_indices, current_index = [], [], 0

for i, c in enumerate(data):
    [file_indices, free_space_indices][i % 2] += [[*range(current_index, current_index := current_index + int(c))]]

          
for y in reversed(range(len(file_indices))):
    for x in range(len(free_space_indices)):
        if len(free_space_indices[x]) >= len(file_indices[y]) and file_indices[y][0] > free_space_indices[x][0]:
            file_indices[y] = free_space_indices[x][:len(file_indices[y])]
            free_space_indices[x] = free_space_indices[x][len(file_indices[y]):]

print(sum((i * j) for i, f in enumerate(file_indices) for j in f))