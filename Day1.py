with open('Day1Data.txt', 'r') as f:
    blocks = f.read().split('\n\n')
    blocks = [[int(x) for x in block.split('\n')] for block in blocks]
    totals = [sum(block) for block in blocks]

print('First star:')
print(max(totals))

totals.sort()

print('Second star:')
print(sum(totals[-3:]))