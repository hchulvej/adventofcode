input = []

with open('2023_02_1.txt', 'r') as f:
    for l in f.readlines():
        input.append(l.replace('\n', ''))


games = []


for i in range(len(input)):
    games.append([x.strip() for x in input[i].split(':')[1].split(';')])


def parse_game_example(s):
    s = [x.strip().split(' ') for x in s.split(',')]
    rgb = [0,0,0]
    for i in range(len(s)):
        if s[i][1] == "red":
            rgb[0] = rgb[0] + int(s[i][0])
        if s[i][1] == "green":
            rgb[1] = rgb[1] + int(s[i][0])
        if s[i][1] == "blue":
            rgb[2] = rgb[2] + int(s[i][0])
    return rgb

def parse_game_input(game):
    return [parse_game_example(x) for x in game]

RED = 12
GREEN = 13
BLUE = 14

def check_game(game):
    res = True
    for g in game:
        if g[0] > RED or g[1] > GREEN or g[2] > BLUE:
            res = False
    return res


def partOne():
    score = 0

    for i in range(len(games)):
        if check_game(parse_game_input(games[i])):
            score = score + i + 1    
    print(score)
    
# partOne()

def partTwo():
    score = 0
    for i in range(len(games)):
        parsed_game = parse_game_input(games[i])
        min_red = max([t[0] for t in parsed_game])
        min_green = max([t[1] for t in parsed_game])
        min_blue = max([t[2] for t in parsed_game])
        score = score + min_red * min_green * min_blue
    print(score)

partTwo()