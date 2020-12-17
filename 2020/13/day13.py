import time

TEST_DATA = 'test'
TEST_CASE_1 = 295
SOLUTION_INPUT = 'input'
ANSI_SILVER = '\033[1;37m'
ANSI_GOLD = '\033[1;33m'
ANSI_NC = '\033[0;m'    
EARLIEST_TIMESTAMP = 100000000000000

def get_data(filepath):
    return [line.strip() for line in open(filepath).readlines()]

def silver(filepath):
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

def gold(filepath):
    _, buses = get_data(filepath)
    buses = buses.split(',')
    timestamp = 0
    minutes = 0
    cycle_length = int(buses[0])
    for bus_id in buses[1:]:
        minutes += 1
        if bus_id == 'x':
            continue
        while (timestamp + minutes) % int(bus_id) != 0:
            timestamp += cycle_length
        cycle_length *= int(bus_id) 
    return timestamp    

def solve(solution_method_1, test_case_1, solution_method_2, test_case_2):
    assert solution_method_1(TEST_DATA) == test_case_1
    start_time = time.time()
    print('Part 1: %s%d%s' % (ANSI_SILVER, solution_method_1(SOLUTION_INPUT), ANSI_NC))
    print('Solved in %s seconds' % (time.time() - start_time))
    assert solution_method_2(TEST_DATA) == test_case_2
    start_time = time.time()
    print('Part 2: %s%d%s' % (ANSI_GOLD, solution_method_2(SOLUTION_INPUT), ANSI_NC))
    print('Solved in %s seconds' % (time.time() - start_time))

solve(silver, 295, gold, 1068781)
