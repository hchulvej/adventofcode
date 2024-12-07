import functools

def read_input(input_file):
    with open(input_file) as f:
        lines = [line.strip() for line in f.readlines()]
    return lines

raw_input = read_input("2024_05_1.txt")

ordering = [tuple(map(int,s.split("|"))) for s in raw_input if s.count("|") == 1]
updates = [list(map(int,s.split(","))) for s in raw_input if s.count(",") > 0]

# Part One

order = dict()
for mi, ma in ordering:
    if ma not in order:
        order[ma] = set()
    order[ma].add(mi)

def is_ordered(arr, order):
    ordered = True
    for i in range(len(arr) - 1):
        if arr[i] not in order:
            continue
        if arr[i + 1] in order[arr[i]]:
            ordered = False
            break
    return ordered

sum_part_one = 0
for update in updates:
    if is_ordered(update, order):
        sum_part_one += update[len(update) // 2]

print(sum_part_one)

# Part Two

sum_part_two = 0
not_in_order_updates = [update for update in updates if not is_ordered(update, order)]

def less_than(a, b):
    if a == b:
        return 0
    if (a not in order and b not in order):
        return a - b
    if a in order:
        if b in order[a]:
            return 1
        else:
            return -1
    else:
        if a in order[b]:
            return -1
        else:
            return 1

for update in not_in_order_updates:
    sum_part_two += sorted(update, key=functools.cmp_to_key(less_than))[len(update) // 2]

print(sum_part_two)
    