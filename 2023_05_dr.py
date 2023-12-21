input = []

with open('2023_05_test.txt', 'r') as f:
    input = [x.replace('\n', '') for x in f.readlines() if "map" not in x]
    input.append("")

seed_input = list(map(int, input[0].split(":")[1].strip().split(" ")))

seed_ranges = [(seed_input[i], seed_input[i] + seed_input[i + 1]) for i in range(0, len(seed_input), 2)]

names = ["se-so", "so-fe", "fe-wa", "wa-li", "li-te", "te-hu", "hu-lo"]

src_ranges = []
dst_ranges = []
src_temp = []
dst_temp = []

for line in input[2:]:
    if (len(line) > 0):
        t = tuple(map(int, line.split(" ")))
        src_temp.append((t[1], t[1] + t[2]))
        dst_temp.append((t[0], t[0] + t[2])) 
    else:
        src_ranges.append(src_temp)
        dst_ranges.append(dst_temp)
        src_temp = []
        dst_temp = []
        
        
def translate(input_int, src_range, dst_range):
    untranslated = []
    translated = []
    left_input, right_input = input_int
    left_src, right_src = src_range
    diff = dst_range[0] - src_range[0]
    # Case 1: No intersection
    if right_input <= left_src or right_input <= left_src:
        untranslated.append(input_int)
    # Case 2: Left intersection
    # --src--|
    #      |--------input
    if left_src < left_input and left_input <= right_src < right_input:
        translated.append((left_input + diff, right_src + diff)) # intersection translated
        untranslated.append((right_src, right_input)) # remaining part not translated
    # Case 3: Right intersection
    # --input--|
    #      |-----src
    if left_src < right_input <= right_src and left_input < left_src:
        translated.append((left_src + diff, right_input + diff)) # intersection translated
        untranslated.append((left_input, left_src)) # remaining part not translated
    # Case 4: Full intersection
    # |----- input ------|
    #      |--src--|
    if left_input <= left_src and right_input >= right_src:
        translated.append((left_src + diff, right_src + diff))
        untranslated.append((left_input,left_src))
        untranslated.append((right_src, right_input))
    # Case 5: Full intersection 2
    # |----- src ------|
    #      |--input--|
    if left_src <= left_input and right_src >= right_input:
        translated.append((left_input + diff, right_input + diff))
        
    
    return [translated, untranslated]
    

print(translate((10,20), (15, 25), (18,28)))


