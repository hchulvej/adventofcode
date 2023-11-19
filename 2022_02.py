'''
A: Rock, B: Paper, C: Scissors
X: Rock, Y: Paper, Z: Scissors
Loss: 0, Draw: 3, Win: 6
'''

WIN = {'A' : 'Y', 'B' : 'Z', 'C' : 'X'}
LOSS = {'A' : 'Z', 'B' : 'X', 'C' : 'Y'}

def score(s):
    p = {'X' : 1, 'Y' : 2, 'Z' : 3}[s[-1]]
    print("p = " + str(p))
    
    if s[0] == s[-1]:
        print(s + ' Draw')
        return p + 3
    if s[-1] == WIN[s[0]]:
        print(s + ' Win')
        return p + 6
    if s[-1] == LOSS[s[0]]:
        print(s + ' Loss')
        return p
        
def parse_round_2(s):
    return 0



points_round_1 = 0
points_round_2 = 0
with open('2022_02.txt', 'r') as f:
    for l in f.readlines():
        s = l.replace('\n', '')
        print(score(s))
        
        

print(points_round_1)