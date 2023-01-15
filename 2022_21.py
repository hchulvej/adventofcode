"""
    Load and parse data
    
    'root: pppw + sjmn', 'dbpl: 5'
"""
def parse_line(line: str) -> dict:
    s = line.split(" ")
    res = dict()
    res['name'] = s[0][0:4]
    if len(s) == 2:
        res['type'] = 'shouter'
        res['value'] = int(s[1])
    else:
        res['type'] = 'calculator'
        res['operation'] = s[2]
        res['helper_monkeys'] = [s[1], s[3]]
        res['value'] = None
    return res
        

with open('./2022_21_small.txt', "r", encoding="utf-8") as file:
    data = list()
    for line in file:
        data.append(parse_line(line.strip()))

print(data)