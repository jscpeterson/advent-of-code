import time
from itertools import combinations

def get_data(filepath):
    with open(filepath) as f:
        return [int(line) for line in f]

'''
def part1(values):
    for v1 in values:
        for v2 in values:
            if v1+v2 == 2020:
                return v1*v2
'''

def part1(values):
    pairs = combinations(values, 2)
    for pair in pairs:
        if sum(pair) == 2020:
            return pair[0]*pair[1]

assert part1(get_data('test')) == 514579
start_time = time.time()
print('Part 1: %s' % part1(get_data('input')))
print('Solved in %s seconds' % (time.time() - start_time))

def part2(values):
    pairs = combinations(values, 3)
    for pair in pairs:
        if sum(pair) == 2020:
            return pair[0]*pair[1]*pair[2]

assert part2(get_data('test')) == 241861950
start_time = time.time()
print('\nPart 2: %s' % part2(get_data('input')))
print('Solved in %s seconds' % (time.time() - start_time))
