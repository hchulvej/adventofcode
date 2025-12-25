import numpy as np

def read_data():
    with open("2025_08_test.txt") as f:
        return [[int(n) for n in l.split(",")] for l in f.read().split("\n")]

## Part 1 ##

# Udregner kvadratet af afstanden mellem to punkter i 3D-rum
def distance_calc(p1, p2):
    return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2 + (p1[2] - p2[2]) ** 2

data = read_data()

# Udregner og gemmer alle afstande i en opslagstabel
calculated_distances = { i:[distance_calc(data[i], data[j]) for j in range(i + 1,len(data))] for i in range(len(data) - 1) }

# Funktion til at slå afstand op mellem to punkter ved hjælp af opslagstabellen
def distance_lookup(i, j):
    if i < j:
        return calculated_distances[i][j - i - 1]
    elif i > j:
        return distance_lookup(j, i)
    else:
        return 0

# Matricen indeholdende alle afstande mellem punkter
distance_matrix = np.array([ [ distance_lookup(i,j) for j in range(len(data)) ] for i in range(len(data)) ])

# Punkternes gruppering baseret på afstande
gruppering = { i : [data[i]] for i in range(len(data)) }



def grupper_punkterne():
    mindsteafstand = 0
    runde = 0
    while runde < len(data):
        min_afstand = distance_matrix[distance_matrix > mindsteafstand].min()
        indeks = np.where(distance_matrix == min_afstand)
        for inx in indeks:
            p1, p2 = inx[0], inx[1]
            if p1 < p2:
                gruppering[p1].extend(gruppering[p2])
                gruppering[p2] = []
                print(f"Runde {runde}: Punkt {p2} er nu en del af gruppe {p1}")
        mindsteafstand = min_afstand
        runde += 1

grupper_punkterne()
print(gruppering)
print({ i : len(gruppering[i]) for i in range(len(data)) if len(gruppering[i]) > 0 })

