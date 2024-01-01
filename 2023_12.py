input = open("2023_12_1.in").read().splitlines()

springs = []
groups = []

for line in input:
    sl = line.split(" ")
    springs.append(sl[0])
    groups.append(tuple(map(int, sl[1].split(","))))


memo = dict()

def combs(s, g):
    
    if len(s) == 0:
        if g == ():
            return 1
        else:
            return 0
    
    if g == ():
        if "#" in s:
            return 0
        else:
            return 1
    
    m_key = (s, g)
    
    if m_key in memo:
        return memo[m_key]
    
    res = 0
    
    if s[0] in ".?":
        res += combs(s[1:], g)
    
    if s[0] in "#?": 
        if len(s) >= g[0] and s[:g[0]].count(".") == 0:
            if len(s) == g[0] or s[g[0]] != "#":
                res += combs(s[g[0] + 1:], g[1:])
    
    memo[m_key] = res
    
    return res

print("Part 1:", sum([combs(springs[i], groups[i]) for i in range(len(groups))]))

new_springs = ["?".join(5*[springs[i]]) for i in range(len(springs))]
new_groups = [tuple(5 * list(groups[i])) for i in range(len(groups))]

print("Part 2:", sum([combs(new_springs[i], new_groups[i]) for i in range(len(new_groups))]))

  