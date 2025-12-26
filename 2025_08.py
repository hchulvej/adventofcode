from collections import Counter

def read_data():
    with open("2025_08_test.txt") as f:
        return [[int(n) for n in l.split(",")] for l in f.read().split("\n")]

## Part 1 ##

# Udregner kvadratet af afstanden mellem to punkter i 3D-rum
def distance_calc(p1, p2):
    return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2 + (p1[2] - p2[2]) ** 2

data = read_data()

# Udregner og gemmer alle afstande mellem to punkter i en opslagstabel
calculated_distances = { (i,j) : distance_calc(data[i], data[j]) for i in range(len(data)) for j in range(i + 1, len(data)) }

# Funktion til at slå afstand op mellem to punkter ved hjælp af opslagstabellen
def distance_lookup(i, j):
    if i < j:
        return calculated_distances[(i,j)]
    elif i > j:
        return distance_lookup(j, i)
    else:
        return 0

# Vi sorterer punktparrene baseret på deres afstande, mindste afstand først
sorted_distances = sorted(calculated_distances.keys(), key=lambda pair: calculated_distances[pair])

for i, j in sorted_distances:
    print("i = " + str(i), "j = " + str(j), "Distance squared:", calculated_distances[(i,j)])



