import time
import sys

TEST_DATA = 'test'
TEST_CASE_1 = 37
TEST_CASE_2 = 26
SOLUTION_INPUT = 'input'
ANSI_SILVER = '\033[1;37m'
ANSI_GOLD = '\033[1;33m'
ANSI_PURPLE = '\033[1;34m'
ANSI_MAGENTA = '\033[1;35m'
ANSI_CYAN = '\033[1;36m'
ANSI_NC = '\033[0;m'    
EMPTY = 'L'
OCCUPIED = '#'
FLOOR = '.'
TOO_MANY_NEIGHBORS = 4
TOO_MANY_NEIGHBORS_SEEN = 5
CARDINAL_DIRECTIONS = [
  (0, -1), #north
  (1, -1), #northeast
  (1, 0), #east
  (1, 1), #southeast
  (0, 1), #south
  (-1, 1), #southwest
  (-1, 0), #west
  (-1, -1) #northwest
]

def get_data(filepath):
    return [line.strip() for line in open(filepath).readlines()]

def seat_in_ferry(seat, max_x, max_y):
    seat_x = seat[0]
    seat_y = seat[1]
    return seat_x < max_x and seat_x >= 0 and seat_y < max_y and seat_y >= 0

def build_grid_and_neighbors(ferry, max_x, max_y):
    ferry_grid = dict()
    ferry_neighbors = dict()
    for y, row in enumerate(ferry):
        for x, seat in enumerate(row):
            point = (x, y)
            neighbors = []
            for possible_neighbor in CARDINAL_DIRECTIONS:
                neighbor_x = x + possible_neighbor[0]
                neighbor_y = y + possible_neighbor[1]
                if seat_in_ferry((neighbor_x, neighbor_y), max_x, max_y):
                    neighbors.append((neighbor_x, neighbor_y))
            ferry_neighbors[point] = neighbors
            ferry_grid[point] = seat
    return (ferry_grid, ferry_neighbors)

def solve(filepath, shuffle_method):
    ferry = get_data(filepath)
    max_y = len(ferry)
    max_x = len(ferry[0])
    ferry_grid, ferry_neighbors = build_grid_and_neighbors(ferry, max_x, max_y)
    new_grid = shuffle_method(ferry_grid, ferry_neighbors, max_x, max_y)
    occupado = 0
    for seat in new_grid:
        if new_grid[seat] == OCCUPIED:
            occupado += 1
    return occupado

def print_grid(ferry_grid, max_x, max_y):
    for y in range(0, max_y):
        for x in range(0, max_x):
            sys.stdout.write(ferry_grid[(x,y)])
        sys.stdout.write('\n')

def seat_shuffle_by_neighbors(ferry_grid, ferry_neighbors, max_x, max_y, too_many_neighbors=TOO_MANY_NEIGHBORS):
    """Shuffles based on occupied neighbors. too_many_neighbors represents # of neighbors that causes a seat change"""
    new_grid = ferry_grid.copy()
    changed_seats = 0
    for ferry_seat in ferry_grid:
        if ferry_grid[ferry_seat] == EMPTY:
            # If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
            if all(ferry_grid[neighbor] != OCCUPIED for neighbor in ferry_neighbors[ferry_seat]):
                new_grid[ferry_seat] = OCCUPIED
                changed_seats += 1
        elif ferry_grid[ferry_seat] == OCCUPIED:
            # If a seat is occupied (#) and four or more seats adjacent to it are also occupied, the seat becomes empty.
            occupied_seats = []
            for neighbor in ferry_neighbors[ferry_seat]:
                if ferry_grid[neighbor] == OCCUPIED:
                    occupied_seats.append(neighbor)
            if len(occupied_seats) >= too_many_neighbors:
                new_grid[ferry_seat] = EMPTY
                changed_seats += 1
        else:
            # Otherwise, the seat's state does not change.
            pass
    # print_grid(new_grid, max_x, max_y)
    # print('\n')
    if changed_seats == 0:
        return new_grid
    else:
        return seat_shuffle_by_neighbors(new_grid, ferry_neighbors, max_x, max_y, too_many_neighbors)

def get_seats_in_los(vantage_point, ferry_grid, max_x, max_y):
    """Returns a list of first seats seen in the line of sight of vantage_point"""
    seats_in_los = []
    for direction in CARDINAL_DIRECTIONS:
        seat_in_los = (vantage_point[0] + direction[0], vantage_point[1] + direction[1])
        if seat_in_ferry(seat_in_los, max_x, max_y):
            seats_in_los.append(seat_in_los)
            seen_seat = ferry_grid[seat_in_los]
            while seen_seat != EMPTY and seen_seat != OCCUPIED:
                seat_in_los = (seat_in_los[0] + direction[0], seat_in_los[1] + direction[1])
                if seat_in_ferry(seat_in_los, max_x, max_y):
                    seen_seat = ferry_grid[seat_in_los]
                    seats_in_los.append(seat_in_los)
                else:
                    break
    return seats_in_los

def visualize_los(vantage_point, ferry_grid, max_x, max_y):
    '''Prints grid from vantage_point as purple, highlighting LOS as magenta'''
    seats_in_los = get_seats_in_los(vantage_point, ferry_grid, max_x, max_y)
    for y in range(0, max_y):
        for x in range(0, max_x):
            if (x,y) == vantage_point:
                color = ANSI_PURPLE
            elif (x,y) in seats_in_los:
                color = ANSI_MAGENTA
            else:
                color = ANSI_NC
            sys.stdout.write('%s%s%s' % (color, ferry_grid[(x,y)], ANSI_NC))
        sys.stdout.write('\n')

def seat_shuffle_by_vision(ferry_grid, ferry_neighbors, max_x, max_y, too_many_neighbors_seen=TOO_MANY_NEIGHBORS_SEEN):
    """Shuffles based on neighbors seen in LOS. too_many_neighbors represents # of neighbors that causes a seat change"""
    new_grid = ferry_grid.copy()
    changed_seats = 0
    for ferry_seat in ferry_grid:
        # visualize_los(ferry_seat, ferry_grid, max_x, max_y)
        # print('\n')
        if ferry_grid[ferry_seat] == EMPTY:
            # empty seats that see no occupied seats become occupied
            if all(ferry_grid[neighbor] != OCCUPIED for neighbor in get_seats_in_los(ferry_seat, ferry_grid, max_x, max_y)):
                new_grid[ferry_seat] = OCCUPIED
                changed_seats += 1
        elif ferry_grid[ferry_seat] == OCCUPIED:
            # it now takes five or more visible occupied seats for an occupied seat to become empty
            occupied_seats = []
            for neighbor in get_seats_in_los(ferry_seat, ferry_grid, max_x, max_y):
                if ferry_grid[neighbor] == OCCUPIED:
                    occupied_seats.append(neighbor)
            if len(occupied_seats) >= too_many_neighbors_seen:
                new_grid[ferry_seat] = EMPTY
                changed_seats += 1
        else:
            # empty seats that see no occupied seats become occupied, seats matching no rule don't change, and floor
            # never changes.
            pass
    # print_grid(new_grid, max_x, max_y)
    # print('\n')
    if changed_seats == 0:
        return new_grid
    else:
        return seat_shuffle_by_vision(new_grid, ferry_neighbors, max_x, max_y, too_many_neighbors_seen)

assert solve(TEST_DATA, seat_shuffle_by_neighbors) == TEST_CASE_1
start_time = time.time()
print('Part 1: %s%d%s' % (ANSI_SILVER, solve(SOLUTION_INPUT, seat_shuffle_by_neighbors), ANSI_NC))
print('Solved in %s seconds' % (time.time() - start_time))
assert solve(TEST_DATA, seat_shuffle_by_vision) == TEST_CASE_2
start_time = time.time()
print('Part 2: %s%d%s' % (ANSI_GOLD, solve(SOLUTION_INPUT, seat_shuffle_by_vision), ANSI_NC))
print('Solved in %s seconds' % (time.time() - start_time))