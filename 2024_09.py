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

file_system = populate_file_system(data)

def min_index_free_space(fs, fl):
    left_index = 0
    try:
        left_index = fs.index(".", left_index)
    except ValueError:
        left_index = len(fs)
    while left_index + fl < len(fs):
        if fs[left_index:left_index + fl].count(".") >= fl:
            return left_index
        try:
            left_index = fs.index(".", left_index + fl)
        except ValueError:
            left_index = len(fs)
    return len(fs)
    
      
i = len(file_system) - 1
moved = set()
while i > 0:
    if file_system[i] == ".":
        i -= 1
    else:
        f_name = file_system[i]
        f_length = file_system.count(f_name)
        fs_min_index = min_index_free_space(file_system, f_length)
        if fs_min_index < len(file_system) and (f_name not in moved) and fs_min_index < i:
            moved.add(f_name)
            for j in range(f_length):
                file_system[fs_min_index + j] = f_name
                file_system[i - j] = "."
        else:
            i -= f_length
            
score_part_two = 0

for i, item in enumerate(file_system):
    if item != ".":
        score_part_two += int(item) * i

print(f"Score part two: {score_part_two}")
          
