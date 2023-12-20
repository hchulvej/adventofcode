input = []

with open('2023_05_test.txt', 'r') as f:
    input = [x.replace('\n', '') for x in f.readlines() if "map" not in x]
    input.append("")

seed_input = list(map(int, input[0].split(":")[1].strip().split(" ")))

seed_ranges = [(seed_input[i], seed_input[i] + seed_input[i + 1]) for i in range(0, len(seed_input), 2)]

names = ["se-so", "so-fe", "fe-wa", "wa-li", "li-te", "te-hu", "hu-lo"]

src_ranges = [set()]*7
dst_ranges = [set()]*7

i = 0

for line in input[2:]:
    if (len(line) > 0):
        print(i)
        src_ranges[i].add(line)
        dst_ranges[i].add(line)
    else:
        i += 1
        
        

print(src_ranges[0])     




