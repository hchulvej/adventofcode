def read_input(input_file):
    with open(input_file) as f:
        lines = [list(line.strip()) for line in f.readlines()]
    return lines

raw_input = read_input("2024_09_1.txt")

data = list(map(int, raw_input[0]))

# Part One

def populate_file_system(data, part=1):
    file = []
    
    current_index = 0
    for i, val in enumerate(data):
        if i % 2 == 0:
            if part == 1:
                file += [str(current_index)] * val
            else:
                file.append([str(current_index), val])
            current_index += 1
        else:
            if part == 1:
                file += ["."] * val
            else:
                file.append(["Free space", val])
        
    return file

def print_file_system(fs):
    test = ""

    for i, item in enumerate(fs):
        if item[0] == "Free space":
            for _ in range(item[1]):
                test += "."
        else:
            for _ in range(item[1]):
                test += item[0]    
    return test

def combine_free_space(fs):
    for _ in range(len(fs)):
        for i, item in enumerate(fs):
            if item[0] == "Free space" and i < len(fs) - 1 and fs[i + 1][0] == "Free space":
                fs[i][1] += fs[i + 1][1]
                fs.pop(i + 1)
    return fs
                  

def compact_file_system(file, part=1):
    if part == 1:
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
    else:
        right_index = len(file) - 1
        while right_index >= 0:
            while file[right_index][0] == "Free space":
                right_index -= 1
            for i in range(right_index):
                if file[i][0] != "Free space" or file[i][1] < file[right_index][1]:
                    continue
                else:
                    tmp = file[right_index].copy()
                    file[right_index][0] = "Free space"
                    file.insert(i, tmp)
                    file[i + 1][1] -= tmp[1]
                    file = combine_free_space(file)
            right_index -= 1
        return file
                    

def score(data_file):
    compacted_file = compact_file_system(populate_file_system(data_file))
    eof = compacted_file.index(".")
    checksum = 0
    for i in range(eof):
        checksum += int(compacted_file[i]) * i
    return checksum
        
    
print(score(data))    


# Part Two

#print(populate_file_system(data, part=2))
#print(print_file_system(compact_file_system(populate_file_system(data, part=2), part=2)))

checksum = 0
current_index = 0
for item in compact_file_system(populate_file_system(data, part=2), part=2):
    for _ in range(item[1]):
        if item[0] != "Free space":
            checksum += int(item[0]) * current_index
        current_index += 1

print(checksum)
        

          
