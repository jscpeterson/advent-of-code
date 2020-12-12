import time

TEST_DATA = 'test'
SOLUTION_INPUT = 'input'
ANSI_SILVER = '\033[1;37m'
ANSI_GOLD = '\033[1;33m'
ANSI_NC = '\033[0;m'    

def get_instructions(filepath):
    return [(line.strip()[:1], int(line.strip()[1:])) for line in open(filepath).readlines()]

def manhattan(point1, point2):
    x1 = point1[0]
    y1 = point1[1]
    x2 = point2[0]
    y2 = point2[1]
    return abs(x1-x2) + abs(y1-y2)

# Action N means to move north by the given value.
# Action S means to move south by the given value.
# Action E means to move east by the given value.
# Action W means to move west by the given value.
# Action L means to turn left the given number of degrees.
# Action R means to turn right the given number of degrees.
# Action F means to move forward by the given value in the direction the ship is currently facing.

EAST = 0
SOUTH = 1
WEST = 2
NORTH = 3
START_DIRECTION = EAST
TURNS = {
    90: 1,
    180: 2,
    270: 3,
    360: 4,
}

def move_north(point, value):
    return (point[0], point[1]-value, point[2])

def move_south(point, value):
    return (point[0], point[1]+value, point[2])

def move_east(point, value):
    return (point[0]+value, point[1], point[2])

def move_west(point, value):
    return (point[0]-value, point[1], point[2])

def turn_left(point, value):
    return (point[0], point[1], (point[2] - TURNS[value]) % len(TURNS))

def turn_right(point, value):
    return (point[0], point[1], (point[2] + TURNS[value]) % len(TURNS))

def move_forward(point, value):
    direction = point[2]
    if direction == EAST:
        return move_east(point, value)
    elif direction == SOUTH:
        return move_south(point, value)
    elif direction == WEST:
        return move_west(point, value)
    elif direction == NORTH:
        return move_north(point, value)
    else:
        raise Exception("direction %s not recognized" % (direction))

ACTIONS = {
   'N':move_north,
   'S':move_south,
   'E':move_east,
   'W':move_west,
   'L':turn_left,
   'R':turn_right,
   'F':move_forward,
}

def letsgo(filepath):
    ship_direction = START_DIRECTION
    ship_origin = (0, 0) # ??
    ship_location = (ship_origin[0], ship_origin[1], ship_direction) 
    instructions = get_instructions(filepath)
    for instruction in instructions:
        action = instruction[0]
        value = instruction[1]
        ship_location = ACTIONS[action](ship_location, value)
    return manhattan(ship_origin, ship_location)


def solve(solution_method_1, test_case_1, solution_method_2, test_case_2):
    assert solution_method_1(TEST_DATA) == test_case_1
    start_time = time.time()
    print('Part 1: %s%d%s' % (ANSI_SILVER, solution_method_1(SOLUTION_INPUT), ANSI_NC))
    print('Solved in %s seconds' % (time.time() - start_time))
    #assert solution_method_2(TEST_DATA) == test_case_2
    #start_time = time.time()
    #print('Part 2: %s%d%s' % (ANSI_GOLD, solution_method_2(SOLUTION_INPUT), ANSI_NC))
    #print('Solved in %s seconds' % (time.time() - start_time))

solve(letsgo, 25, None, None)
