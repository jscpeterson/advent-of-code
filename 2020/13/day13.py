import time

TEST_DATA = 'test'
TEST_CASE_1 = 295
SOLUTION_INPUT = 'input'
ANSI_SILVER = '\033[1;37m'
ANSI_GOLD = '\033[1;33m'
ANSI_NC = '\033[0;m'    

def get_data(filepath):
    return [line.strip() for line in open(filepath).readlines()]

def letsgo(filepath):
    earliest, buses = get_data(filepath)
    earliest = int(earliest)
    buses = buses.split(',')
    buses = [int(bus) for bus in buses if bus != 'x']
    best_bus = None
    time = earliest
    while True:
        for bus in buses:
            if time % bus == 0:
                best_bus = bus
                minutes_to_wait = time - earliest
                return(minutes_to_wait * best_bus)
        time += 1

print(letsgo('test'))

def solve(solution_method_1, test_case_1, solution_method_2, test_case_2):
    assert solution_method_1(TEST_DATA) == test_case_1
    start_time = time.time()
    print('Part 1: %s%d%s' % (ANSI_SILVER, solution_method_1(SOLUTION_INPUT), ANSI_NC))
    print('Solved in %s seconds' % (time.time() - start_time))
    #assert solution_method_2(TEST_DATA) == test_case_2
    #start_time = time.time()
    #print('Part 2: %s%d%s' % (ANSI_GOLD, solution_method_2(SOLUTION_INPUT), ANSI_NC))
    #print('Solved in %s seconds' % (time.time() - start_time))

solve(letsgo, 295, None, None)
