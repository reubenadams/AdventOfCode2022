import numpy as np

with open('Day5Data.txt', 'r') as f:
    lines = f.read().split('\n')
breakline = lines.index('')

horizontal_stacks = [list(line) for line in lines[:breakline - 1]]
vertical_stacks = [list(stack) for stack in np.array(horizontal_stacks).transpose()]

stacks = []
for messy_upsidedown_stack in vertical_stacks:
    if set(messy_upsidedown_stack).issubset({' ', '[', ']'}):
        continue
    clean_rightwayup_stack = [char for char in reversed(messy_upsidedown_stack) if char not in {' ', '[', ']'}]
    stacks.append(clean_rightwayup_stack)
print(stacks)


# transposed_stacks = np.array().transpose()
# stacks = list()
# for row in transposed_stacks:
#     if set(row).issubset({' ', '[', ']'}):
#         continue
#     else:
#         stacks.append(list(reversed(list((row)))))


# def strip_trailing_spaces(char_list):
#     if ' ' not in char_list:
#         return char_list
#     return char_list[:char_list.index(' ')]
# stacks = [strip_trailing_spaces(stack) for stack in stacks]


def parse_instruction(instruction):
    elements = instruction.split()
    num_move, move_from, move_to = int(elements[1]), int(elements[3]), int(elements[5])
    return num_move, move_from, move_to


instructions = lines[breakline + 1:]
instructions = [parse_instruction(ins) for ins in instructions]


def execute_step(stacks, num_move, move_from, move_to):
    # for i in range(num_move):
    #     block_to_move = stacks[move_from - 1][-1]
    #     stacks[move_from - 1] = stacks[move_from - 1][:-1]
    #     stacks[move_to - 1].append(block_to_move)
    blocks_to_move = stacks[move_from - 1][-num_move:]
    num_left = len(stacks[move_from - 1]) - num_move
    stacks[move_from - 1] = stacks[move_from - 1][:num_left]
    stacks[move_to - 1] = stacks[move_to - 1] + blocks_to_move
    return stacks

print('Start moving')
print(stacks)
for ins in instructions:
    num_move, move_from, move_to = ins
    stacks = execute_step(stacks, num_move, move_from, move_to)
    print(stacks)

print(''.join(stack[-1] for stack in stacks))