import networkx as nx
from graphlib import TopologicalSorter
import numpy as np

def read_data():
    with open("2025_11.txt") as f:
        res = dict()
        for line in f.read().split("\n"):
            key, val = line.strip().split(": ")
            val = val.strip().split(" ")
            res[key.strip()] = val
        return res

data = read_data()

## Part 1 ##

G = nx.DiGraph()

for node, edges in data.items():
    for edge in edges:
        G.add_edge(node, edge)

def no_paths_between(graph, source, target, part=1):
    no_paths = 0
    
    if part == 1:
        for path in nx.all_simple_paths(graph, source=source, target=target):
            no_paths += 1

    return no_paths

print("Part 1:", no_paths_between(G, "you", "out", part=1))

## Part 2 ##

# path: https://topaz.github.io/paste/#XQAAAQAEBAAAAAAAAAAzHIoib6ptmPAUgo2LUPPU+liMkqlgTzuvOgU1YY2MR6L1z1EsGAiR2HjPV0kYxjhiRRH2QsBNB1w3ZL2J2ZsR6djNlUpAUKgQql1muHh48eVhrbOqwUWkWhYyfEyFT9aWd18qs3EDfbIs+3jIpL8eZrRHz5xD6PjstLkkVeAg29VXxutaYevDlG80/qV5HDvHnkGA/OypwOcCu7yN/+ZanOZTWPy35bH8pYiBSGHH1EDMcL5rv1Su3djm7ifRwWePfSpzm/1A+XQu/Ii/RYSxg5kShM1PfWGsWH+0F5u8SFbm+MmUPEsWyvdgOkvDGVS9QF9fHMhQO8iGJVE4jxW4E+DXrIYL/6YL3Nn9BGhIh8OHRUDL1x8UeXWrYZbX/AqN9AE1qjhwM9rKKLvJyY/91ULwip9LJUOjkGi2JTo+OfGspe4a/t19pnPGsiXOMKlXntrpyaTNIRZlZU9hTl6CQovOzLZLdN/U3TXegWCJNvi64gPvlSo1HIXRlH01nAHIhEDiXTFONLf7sSNH/jobn1xsnkmNvJq/XrSEjwAH2KRSo5+WZqiCzv8O3G5EGPYJSOZLcPprQnQdsCDTF7KLTwOXZ7neOIQEGPVlo2ZojSsYdTqqd9vRO6xc11wWHAn9vcHZx8hHU6e//oaOQEs2/FJy7A==

def count_paths(graph, idx, idy):
    ts = TopologicalSorter(graph)
    toposort = list(ts.static_order())[::-1]
    idx, idy = toposort.index(idx), toposort.index(idy)
    counts = np.zeros((len(toposort,)))
    for i in range(len(toposort)-1):
        if i < idx:
            continue
        elif i == idx:
            counts[i] = 1
        for j in graph[toposort[i]]:
            counts[toposort.index(j)] += counts[i]
    return counts[idy]

p2 = count_paths(data, "svr", "fft") * count_paths(data, "fft", "dac") * count_paths(data, "dac", "out")
print(f"Part 2: {int(p2)}")
