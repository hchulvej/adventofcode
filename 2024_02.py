# Part One

def parse_line(line):
    vals = line.strip().split()
    return [int(v) for v in vals]

def read_input(input_file):
    with open(input_file) as f:
        lines = [parse_line(line) for line in f.readlines()]
    return lines

def safety_check(line):
    differences = [line[i + 1] - line[i] for i in range(len(line) - 1)]
    no_pos = len([d for d in differences if (d > 0 and d < 4)])
    no_neg = len([d for d in differences if (d < 0 and d > -4)])
    return (no_pos == len(differences) or no_neg == len(differences))
        
parsed_input = read_input("2024_02_1.txt")

print(len([line for line in parsed_input if safety_check(line)]))

# Part Two

unsafe_levels = [line for line in parsed_input if not safety_check(line)]

def one_item_removed(line):
    arr = []
    for i in range(len(line)):
        arr.append(line[:i] + line[i + 1:])
    return arr

def safe_if_one_level_removed(line):
    return any([safety_check(l) for l in one_item_removed(line)])

still_unsafe = [unsafe for unsafe in unsafe_levels if not safe_if_one_level_removed(unsafe)]

#for unsafe in still_unsafe:
#    print(unsafe, [unsafe[i + 1] - unsafe[i] for i in range(len(unsafe) - 1)])


print(1000 - len(still_unsafe))