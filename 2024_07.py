

def read_input(input_file):
    with open(input_file) as f:
        lines = [line.strip() for line in f.readlines()]
    return lines

raw_input = read_input("2024_07_1.txt")

def parse_line(line):
    test_value, operands = map(lambda s: s.split(" "), line.split(": "))
    operands = list(map(int, operands))
    test_value = int(test_value[0])
    return test_value, operands

data = [parse_line(line) for line in raw_input]

# Part One

def test_value(input_operands, operators, target_value):
    if len(input_operands) != len(operators) + 1:
        return False
    result = input_operands[0]
    for i in range(len(operators)):
        match operators[i]:
            case "+":
                result += input_operands[i + 1]
            case "*":
                result *= input_operands[i + 1]
            
    return result == target_value
    

def combinations(n):
    res = ["+", "*"]
    if n == 1:
        return res
    for _ in range(n - 1):
        res = [r + "+" for r in res] + [r + "*" for r in res]
    return [tuple(r) for r in res]
    

def check_line(line):
    target_value, input_operands = line
    for operators in combinations(len(input_operands) - 1):
        if test_value(input_operands, operators, target_value):
            return True


print(sum([line[0] for line in data if check_line(line)]))   