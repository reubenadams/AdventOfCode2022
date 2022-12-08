with open('Day3Data.txt', 'r') as f:
    sacks = f.read().split()
print(sacks[:5])


priority_dict = dict()
for i in range(1, 27):
    priority_dict[chr(i+96)] = i
for i in range(27, 53):
    priority_dict[chr(i+38)] = i
print(priority_dict)


def common_letter(sack):
    L = len(sack) // 2
    comp1, comp2 = sack[:L], sack[L:]
    common = set(comp1).intersection(set(comp2))
    return list(common)[0]


total_priorities = sum([priority_dict[common_letter(sack)] for sack in sacks])
print('First star:')
print(total_priorities)


total_priorities = 0
for i in range(len(sacks) // 3):
    print(i)
    sack1 = set(sacks[3*i])
    sack2 = set(sacks[3*i + 1])
    sack3 = set(sacks[3*i + 2])
    badge = list(sack1.intersection(sack2).intersection(sack3))[0]
    total_priorities += priority_dict[badge]
print('Second star:')
print(total_priorities)

