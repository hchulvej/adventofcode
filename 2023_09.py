input = open("2023_09_test.in").read().splitlines()
sequences = [list(map(int, s.split(" "))) for s in input]

def all_zeroes(l):
    return min(l) == 0 and max(l) == 0

test_seq = sequences[0]
current_sequence = test_seq.copy()
derived_sequences = [test_seq]
while not all_zeroes(current_sequence):
    current_sequence = [current_sequence[i + 1] - current_sequence[i] for i in range(len(current_sequence) - 1)]
    derived_sequences.append(current_sequence)

for i in range(len(derived_sequences))[::-1]:
    if i == 0:
        derived_sequences[i].append(0)
    else:
        derived_sequences[i - 1].append(derived_sequences[i - 1][-1] + derived_sequences[i][-1])

for seq in derived_sequences:
    print(seq)