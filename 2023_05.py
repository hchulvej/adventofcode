input = []

with open('2023_05_test.txt', 'r') as f:
    input = [x.replace('\n', '') for x in f.readlines() if "map" not in x]
    input.append("")

seed_input = list(map(int, input[0].split(":")[1].strip().split(" ")))

map_inputs = []
temp = []

def convert_to_intervals(arr):
    return [(arr[1], arr[1] + arr[2]), (arr[0], arr[0] + arr[2])]

for x in input[2:]:
    
    if len(x) == 0:
        map_inputs.append(temp)
        temp = []
    else:   
        temp.append(convert_to_intervals(list(map(int, x.split(" ")))))


## PART 1
def convert_seed(seed):
    for maps in map_inputs:
        for xy in maps:
            if seed in range(xy[0][0], xy[0][1]):
                seed = xy[1][0] + seed - xy[0][0]
                break
    return seed
        

print("Part 1: " + str(min([convert_seed(s) for s in seed_input])))

## PART 2
def intersection(intv, map_int):
    a, b = intv
    c, d = map_int[0]
    le = max(a, c)
    re = min(b, d)
    if le >= re:
        return (0,0)
    else:
        e, f  = map_int[1]
        return (e + le - c, e + re - c)

seed_input_ranges = [set()]*8
seed_input_ranges[0] = set([(seed_input[i], seed_input[i] + seed_input[i + 1]) for i in range(0, len(seed_input), 2)])


for i in range(0, 7):
    for map_int in map_inputs[i]:
        for seed_int in seed_input_ranges[i]:
            temp = set()
            temp.add(intersection(seed_int, map_int))
        seed_input_ranges[i + 1] = temp

print(seed_input_ranges)


    
    




