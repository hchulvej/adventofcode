grids = open("2023_13_test.in").read().split("\n\n")

def rows(g):
    return g.split("\n")

def cols(g):
    g_rows = rows(g)
    return ["".join([g_rows[i][j] for j in range(len(g_rows[i]))]) for i in range(len(g_rows))]   
    
def array_comp(str_1, str_2, offset):
    if len(str_1) != len(str_2):
        return False
    diffs = 0
    
    for i, e in enumerate(list(str_1)):
        if e != str_2[i]:
            diffs += 1
    return offset == diffs

def possible_lines(arr, offset):
    return [i for i in range(len(arr) - 1) if array_comp(arr[i], arr[i + 1], offset)]

def horizontal_lines(g):
    return 0

def vertical_lines(g):
    return 0
    
for g in grids:
    print(possible_lines(rows(g), 1))
    print(possible_lines(cols(g), 1))    
