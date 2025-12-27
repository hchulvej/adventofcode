

def read_data():
    with open("2025_09.txt") as f:
        res = []
        for l in f.read().split("\n"):
            if l.strip():
                res.append([int(n) for n in l.split(",")])
        return res

data = read_data()

## Part 1 ##

def rectangle(p1, p2):
    return (abs(p2[0] - p1[0]) + 1) * (abs(p2[1] - p1[1]) + 1)

# Genererer alle punktpar
pairs = [(data[i], data[j]) for i in range(len(data)) for j in range(i + 1, len(data))]
# Sorterer punktparrene baseret på rektangelstørrelse
sorted_pairs = sorted(pairs, key=lambda pair: rectangle(pair[0], pair[1]))

print("Part 1: ",rectangle(sorted_pairs[-1][0], sorted_pairs[-1][1]))

## Part 2 ##

# Too difficult for now