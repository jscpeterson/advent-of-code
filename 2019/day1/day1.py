from math import floor
from utils import get_data, test

test_cases1 = {12:2, 14:2, 1969:654, 100756:33583}

def solve(filepath, function):
    return sum(function(int(line)) for line in get_data(filepath))

def get_fuel(mass):
    return floor(mass/3) - 2

assert test(test_cases1, get_fuel)
print('Part 1: Total fuel needed: %i' % solve('input', get_fuel))

def get_all_fuel(mass):
    fuel = get_fuel(mass)
    if fuel <= 0:
        return 0
    return fuel + get_all_fuel(fuel)

test_cases2 = {14:2, 1969:966, 100756:50346}

assert test(test_cases2, get_all_fuel)
print('Part 2: Total fuel needed: %i' % solve('input', get_all_fuel))

