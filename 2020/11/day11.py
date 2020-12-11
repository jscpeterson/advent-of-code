import time
import sys

TEST_DATA = 'test'
TEST_CASE_1 = 37
SOLUTION_INPUT = 'input'
ANSI_SILVER = '\033[1;37m'
ANSI_GOLD = '\033[1;33m'
ANSI_NC = '\033[0;m'    
EMPTY = 'L'
OCCUPIED = '#'
FLOOR = '.'
NEIGHBORS = [
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

def build_grid_and_neighbors(ferry, max_x, max_y):
    ferry_grid = dict()
    ferry_neighbors = dict()
    for y, row in enumerate(ferry):
        for x, seat in enumerate(row):
            point = (x, y)
            neighbors = []
            for possible_neighbor in NEIGHBORS:
                neighbor_x = x + possible_neighbor[0]
                neighbor_y = y + possible_neighbor[1]
                if neighbor_x < max_x and neighbor_x >= 0 and neighbor_y < max_y and neighbor_y >= 0:
                    neighbors.append((neighbor_x, neighbor_y))
            ferry_neighbors[point] = neighbors
            ferry_grid[point] = seat
    return (ferry_grid, ferry_neighbors)

def solve1(filepath):
    ferry = get_data(filepath)
    max_y = len(ferry)
    max_x = len(ferry[0])
    ferry_grid, ferry_neighbors = build_grid_and_neighbors(ferry, max_x, max_y)
    new_grid = change_seats(ferry_grid, ferry_neighbors, max_x, max_y)
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

def change_seats(ferry_grid, ferry_neighbors, max_x, max_y):
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
            if len(occupied_seats) >= 4:
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
        return change_seats(new_grid, ferry_neighbors, max_x, max_y)


assert solve1(TEST_DATA) == TEST_CASE_1
start_time = time.time()
print('Part 1: %s%d%s' % (ANSI_SILVER, solve1(SOLUTION_INPUT), ANSI_NC))
print('Solved in %s seconds' % (time.time() - start_time))
# assert solution_method_2(TEST_DATA) == test_case_2
# start_time = time.time()
# print('Part 2: %s%d%s' % (ANSI_GOLD, solution_method_2(SOLUTION_INPUT), ANSI_NC))
# print('Solved in %s seconds' % (time.time() - start_time))
