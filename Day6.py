with open('Day6Data.txt', 'r') as f:
    stream = f.read()


def correct_index(stream, unique_seq_len):
    for i in range(len(stream)):
        fourple = stream[i:i+unique_seq_len]
        if len(set(fourple)) == unique_seq_len:
            return i + unique_seq_len


print('First star:')
print(correct_index(stream, 4))
print('Second star:')
print(correct_index(stream, 14))