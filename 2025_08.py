from collections import Counter
import math

def read_data():
    with open("2025_08.txt") as f:
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

# Vi har lånt en datastruktur fra union-find algoritmen til at holde styr på hvilke punkter der er forbundet
class UnionFind:
    def __init__(self, size):
      
        # Initialize the parent array with each 
        # element as its own representative
        self.parent = list(range(size))
    
    def find(self, i):
      
        # If i itself is root or representative
        if self.parent[i] == i:
            return i
          
        # Else recursively find the representative 
        # of the parent
        return self.find(self.parent[i])
    
    def unite(self, i, j):
      
        # Representative of set containing i
        irep = self.find(i)
        
        # Representative of set containing j
        jrep = self.find(j)
        
        # Make the representative of i's set
        # be the representative of j's set
        self.parent[irep] = jrep

# Vi forbinder de 10 tætteste punkter
uf = UnionFind(len(data))
for (i, j) in sorted_distances[:1000]:
    uf.unite(i, j)

values = [uf.find(i) for i in range(len(data))]
counter = Counter(values)

print("Part 1:", math.prod([e[1] for e in counter.most_common(3)]))

## Part 2 ##

# Vi fortsætter med at forbinde punkter, indtil alle punkter er forbundet
uf2 = UnionFind(len(data))
for (i, j) in sorted_distances:
    uf2.unite(i, j)
    # Finder alle værdier
    values = [uf2.find(k) for k in range(len(data))]
    # Tæller forekomsterne af hver værdi
    counter = Counter(values)
    # Hvis der kun er én unik værdi, er alle punkter forbundet
    if len(counter) == 1:
        print("Part 2:", data[i][0] * data[j][0])
        break