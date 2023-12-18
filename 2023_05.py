input = []

with open('2023_05_1.txt', 'r') as f:
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




