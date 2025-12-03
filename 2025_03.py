def read_data():
    with open("2025_03.txt") as f:
        return f.read().split("\n")


data = read_data()



## Part 1
def joltage_ratings(data_line):
    values = set(int(x) for x in list(data_line))
    return {x : sorted([i for i in range(len(data_line)) if int(data_line[i]) == x]) for x in values}

def output_joltage(data_line):
    joltage_dict = joltage_ratings(data_line)
    max_val_10 = 9
    while max_val_10 not in joltage_dict or min(joltage_dict[max_val_10]) == len(data_line) - 1:
        max_val_10 -= 1
    max_val_1 = 9
    while max_val_1 not in joltage_dict or max(joltage_dict[max_val_1]) <= min(joltage_dict[max_val_10]):
        max_val_1 -= 1
    return max_val_10 * 10 + max_val_1    
        

def total_joltage():
    total = 0
    for data_line in list(data):
        total += output_joltage(data_line)
    return total    

print("Total output joltage for part 1: ", total_joltage())


## Part 2
def output_joltage_part2(data_line):
    vals = []
    new_data_line = data_line[:]
    lowest_index = 0
    for d in range(12, 0, -1):
        highest_index = len(new_data_line) - d
        joltage_dict = joltage_ratings(new_data_line)
        max_val = max(k for k in joltage_dict.keys() if min(joltage_dict[k]) <= highest_index and max(joltage_dict[k]) >= lowest_index)
        vals.append(max_val)
        lowest_index = joltage_dict[max_val][0] + 1
        new_data_line = "".join(["0" for _ in range(lowest_index)] + list(new_data_line[lowest_index:]))
    return int("".join([str(x) for x in vals]))
        
           
def total_joltage_part2():
    total = 0
    for data_line in list(data):
        total += output_joltage_part2(data_line)
    return total

print(total_joltage_part2())