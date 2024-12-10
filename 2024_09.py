def read_input(input_file):
    with open(input_file) as f:
        lines = [list(line.strip()) for line in f.readlines()]
    return lines

raw_input = read_input("2024_09_1.txt")

data = list(map(int, raw_input[0]))

def populate_file(data):
    file = []
    current_index = 0
    for i, val in enumerate(data):
        if i % 2 == 0:
            file += [str(current_index)] * val
            current_index += 1
        else:
            file += ["."] * val
        
    return file

def compact_file(file):
    left_index = 0
    right_index = len(file) - 1
    while left_index < right_index:
        while file[left_index] != ".":
            left_index += 1
        while file[right_index] == ".":
            right_index -= 1
        if left_index < right_index:
            tmp = file[right_index]
            file[right_index] = "."
            file[left_index] = tmp
    return file

def score(data_file):
    compacted_file = compact_file(populate_file(data_file))
    eof = compacted_file.index(".")
    checksum = 0
    for i in range(eof):
        checksum += int(compacted_file[i]) * i
    return checksum
        
    
print(score(data))            
    