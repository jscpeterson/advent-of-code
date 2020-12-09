from itertools import combinations

def get_data(filepath):
    return [int(line) for line in open(filepath).readlines()]

def solve1(filepath, preamble):
    inputs = get_data(filepath)
    for i, line in enumerate(inputs):
        if i <= preamble:
            continue
        sums = set(sum(comb) for comb in combinations(inputs[i-preamble:i], 2))
        if line not in sums:
            return line

def solve2(filepath, preamble):
    target = solve1(filepath, preamble)
    inputs = get_data(filepath)
    for i, input1 in enumerate(inputs):
       for i2, input2 in enumerate(inputs[i:]):
            values = inputs[i:i2]
            sum_ = sum(values)
            if sum_ == target:
                 return min(values)+max(values)
            if sum_ > target:
                 break            
                      
assert solve1('test', 5) == 127 
print('Part 1: %d' % solve1('input', 25))
assert solve2('test', 5) == 62
print('Part 2: %s' % solve2('input', 25))
