with open('Day4Data.txt', 'r') as f:
    lines = f.read().split('\n')


def parse_line(line):
    range1, range2 = line.split(',')
    start1, end1 = range1.split('-')
    start2, end2 = range2.split('-')
    return int(start1), int(end1), int(start2), int(end2)


def is_subsumed(start1, end1, start2, end2):
    if start1 <= start2 and end1 >= end2:
        print('first is larger')
        return True
    if start1 >= start2 and end1 <= end2:
        print('second is larger')
        return True
    return False


def is_overlapping(start1, end1, start2, end2):
    return not (end1 < start2 or start1 > end2)



total_subsumed = 0
for line in lines:
    start1, end1, start2, end2 = parse_line(line)
    if is_subsumed(start1, end1, start2, end2):
        total_subsumed += 1
print('First star:')
print(total_subsumed)


total_overlapping = 0
for line in lines:
    start1, end1, start2, end2 = parse_line(line)
    if is_overlapping(start1, end1, start2, end2):
        total_overlapping += 1
print('Second star:')
print(total_overlapping)