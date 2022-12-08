shape_dict = {'A': 'rock', 'B': 'paper', 'C': 'scissors', 'X': 'rock', 'Y': 'paper', 'Z': 'scissors'}
winning_pairs = {('rock', 'scissors'), ('paper', 'rock'), ('scissors', 'paper')}


with open('Day2Data.txt') as f:
    shape_pairs = f.read().split('\n')
    shape_pairs = [tuple(shape_dict[shape] for shape in pair.split()) for pair in shape_pairs]


def shape_score(your_shape):
    if your_shape == 'rock':
        return 1
    if your_shape == 'paper':
        return 2
    return 3


def outcome_score(opponents_shape, your_shape):
    if your_shape == opponents_shape:
        return 3
    if (your_shape, opponents_shape) in winning_pairs:
        return 6
    return 0


def round_score(opponents_shape, your_shape):
    return shape_score(your_shape) + outcome_score(opponents_shape, your_shape)


total_score = sum([round_score(pair[0], pair[1]) for pair in shape_pairs])
print('First star:')
print(total_score)


shape_dict = {'A': 'rock', 'B': 'paper', 'C': 'scissors'}
win_dict = {'X': 'lose', 'Y': 'draw', 'Z': 'win'}
winning_pairs = {('rock', 'scissors'), ('paper', 'rock'), ('scissors', 'paper')}


def winning_move(opponents_shape):
    if opponents_shape == 'rock':
        return 'paper'
    if opponents_shape == 'paper':
        return 'scissors'
    return 'rock'


def losing_move(opponents_shape):
    if opponents_shape == 'rock':
        return 'scissors'
    if opponents_shape == 'paper':
        return 'rock'
    return 'paper'


def correct_move(opponents_shape, instruction):
    if instruction == 'win':
        return winning_move(opponents_shape)
    if instruction == 'draw':
        return opponents_shape
    return losing_move(opponents_shape)


def round_score(opponents_shape, instruction):
    total = 0
    if instruction == 'win':
        total += 6
    if instruction == 'draw':
        total += 3
    your_shape = correct_move(opponents_shape, instruction)
    total += shape_score(your_shape)
    return total


with open('Day2Data.txt') as f:
    shape_pairs = f.read().split('\n')
    shape_pairs = [(shape_dict[pair.split()[0]], win_dict[pair.split()[1]]) for pair in shape_pairs]

print(shape_pairs[:5])


total_score = sum([round_score(pair[0], pair[1]) for pair in shape_pairs])
print('Second star:')
print(total_score)