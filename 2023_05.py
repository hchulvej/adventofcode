input = []

with open('2023_05_1.txt', 'r') as f:
    for l in f.readlines():
        input.append(l.replace('\n', ''))

seeds_to_be_sown = [int(n) for n in input[0].split("seeds: ")[1].split(", ")[0].split(" ")]

almanac = dict()
cat = 0
codes = []

i = 1

while i < len(input):
    if len(input[i]) == 0:
        i += 1
    
    if not input[i][0].isdigit():
        i += 1
    
    while i < len(input) and len(input[i]) > 0 and input[i][0].isdigit():
        codes.append([int(n) for n in input[i].strip().split(" ")])
        i += 1
    
    almanac[cat] = codes
    cat +=1
    codes = []
    

seed_destinations = dict(zip(seeds_to_be_sown, [0] * len(seeds_to_be_sown)))

def parse_intervals(arrs, curr):
    for arr in arrs:
        y = arr[0]
        x = arr[1]
        length = arr[2]
        
        if curr >= x and curr <= x + length - 1:
            return curr - x + y
    
    return curr
    
for seed in seeds_to_be_sown:
    original_seed = seed   
    for i in almanac.keys():
        seed = parse_intervals(almanac[i], seed)
    seed_destinations[original_seed] = seed
        


print("Part 1:", min(seed_destinations.values()))

seed_destinations = dict()
        

for i in range(int(len(seeds_to_be_sown) / 2)):
    start = seeds_to_be_sown[2 * i]
    for j in range(seeds_to_be_sown[2 * i + 1]):
        original_seed = start + j
        seed = start + j
        for k in almanac.keys():
            seed = parse_intervals(almanac[k], seed)
        seed_destinations[original_seed] = seed

print("Part 2:", min(seed_destinations.values()))