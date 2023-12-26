input = open("2023_09_1.in").read().splitlines()
sequences = [list(map(int, s.split(" "))) for s in input]

def all_zeroes(l):
    return min(l) == 0 and max(l) == 0

def last_element(test_seq):
    current_sequence = test_seq.copy()
    derived_sequences = [test_seq]
    while not all_zeroes(current_sequence):
        current_sequence = [current_sequence[i + 1] - current_sequence[i] for i in range(len(current_sequence) - 1)]
        derived_sequences.append(current_sequence)

    derived_sequences.reverse()

    for i in range(1, len(derived_sequences)):
        derived_sequences[i].append(derived_sequences[i][-1] + derived_sequences[i-1][-1])
    
    return derived_sequences[-1][-1]

def first_element(test_seq):
    current_sequence = test_seq.copy()
    derived_sequences = [test_seq]
    while not all_zeroes(current_sequence):
        current_sequence = [current_sequence[i + 1] - current_sequence[i] for i in range(len(current_sequence) - 1)]
        derived_sequences.append(current_sequence)

    derived_sequences.reverse()

    for i in range(1, len(derived_sequences)):
        derived_sequences[i].insert(0, derived_sequences[i][0] - derived_sequences[i-1][0])
    
    return derived_sequences[-1][0]

print("Part 1:", sum([last_element(seq) for seq in sequences]))

print("Part 2:", sum([first_element(seq) for seq in sequences]))

