import time
from itertools import combinations

SUM = 2020

def get_data(filepath):
    with open(filepath) as f:
        return {int(line) for line in f}

def part1(values):
    for value in values:
        diff = SUM - value
        if diff in values:
            return value * diff

assert part1(get_data('test')) == 514579
start_time = time.time()
print('Part 1: %s' % part1(get_data('input')))
print('Solved in %s seconds' % (time.time() - start_time))

def part2(values):
    for value1 in values:
        for value2 in values:
            diff = SUM - (value1 + value2)
            if diff in values:
                return diff * value1 * value2

assert part2(get_data('test')) == 241861950
start_time = time.time()
print('\nPart 2: %s' % part2(get_data('input')))
print('Solved in %s seconds' % (time.time() - start_time))
