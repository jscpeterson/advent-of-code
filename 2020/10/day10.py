import time

SOLUTION_INPUT = 'input'
ANSI_SILVER = '\033[1;37m'
ANSI_GOLD = '\033[1;33m'
ANSI_NC = '\033[0;m'    

def get_data(filepath):
    return [int(line) for line in open(filepath).readlines()]


def solve(adapters):
    # Any given adapter can take an input 1, 2, or 3 jolts lower than its rating and still produce its rated output joltage.
    device_adapter = max(adapters) + 3
    outlet = 0
    one_jolt_differences = []
    three_jolt_differences = []
    adapters.append(outlet)
    adapters.append(device_adapter)
    adapters.sort()
    usable_adapters = adapters[:]
    for voltage in adapters:
         higher_voltage = voltage+1
         if higher_voltage in usable_adapters:
             one_jolt_differences.append((usable_adapters.pop(usable_adapters.index(higher_voltage)), voltage))
             continue
         higher_voltage = voltage+3
         if higher_voltage in usable_adapters:
             three_jolt_differences.append((usable_adapters.pop(usable_adapters.index(higher_voltage)), voltage))
    return len(one_jolt_differences)*len(three_jolt_differences)

assert solve(get_data('test1')) == 7*5
assert solve(get_data('test2')) == 22*10
start_time = time.time()
print('Part 1: %s%d%s' % (ANSI_SILVER, solve(get_data(SOLUTION_INPUT)), ANSI_NC))
print('Solved in %s seconds' % (time.time() - start_time))
#    assert solution_method_2(TEST_DATA) == test_case_2
#    start_time = time.time()
#    print('Part 2: %s%d%s' % (ANSI_GOLD, solution_method_2(SOLUTION_INPUT), ANSI_NC))
#    print('Solved in %s seconds' % (time.time() - start_time))

#solve()
