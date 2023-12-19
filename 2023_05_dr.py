input = []

with open('2023_05_test.txt', 'r') as f:
    input = [x.replace('\n', '') for x in f.readlines() if "map" not in x]
    input.append("")

seed_input = list(map(int, input[0].split(":")[1].strip().split(" ")))

seed_ranges = [(seed_input[i], seed_input[i] + seed_input[i + 1]) for i in range(0, len(seed_input), 2)]

map_inputs = []
temp = []

def convert_to_intervals(arr):
    return [(arr[1], arr[1] + arr[2]), (arr[0], arr[0] + arr[2])]

for x in input[2:]:
    
    if len(x) == 0:
        map_inputs.append(temp)
        temp = []
    else:   
        temp.append(list(map(int, x.split(" "))))

def convert_map(arr):
    return (arr[1], arr[1] + arr[2], arr[0], arr[0] + arr[2])

def maps_to(num, map_tuple):
    if not (num >= map_tuple[0] and num < map_tuple[1]):
        return num
    else:
        diff = num - map_tuple[0]
        return map_tuple[2] + diff

maps = dict()
names = ["se-so", "so-fe", "fe-wa", "wa-li", "li-te", "te-hu", "hu-lo"]
for i, name in enumerate(names):
    maps[name] = set()
    for xy in map_inputs[i]:
        maps[name].add(convert_map(xy))

for seed in seed_input:
    res = str(seed)
    curr = seed
    for name in names:
        for map_tuple in maps[name]:
            dest = maps_to(curr, map_tuple)
            if curr != dest:
                res += "-" + str(dest)
                curr = dest
    print(res)
    




