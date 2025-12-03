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

print(total_joltage())