ORIGIN = (0, 0)
PART_1_SLOPE = (3, 1)
PART_1_TEST = 7
PART_2_SLOPES = [(1, 1),
    (3, 1),
    (5, 1),
    (7, 1),
    (1, 2)]
PART_2_TEST = 336

def get_data(filepath):
    with open(filepath) as f:
        return [line.strip('\n') for line in f]

def solve(grid, x_speed, y_speed):
    trees = 0
    max_x = len(grid[0])
    max_y = len(grid)
    location = ORIGIN
    for line in grid:
        x = (location[0] + x_speed) % max_x
        y = location[1] + y_speed
        if y >= max_y:
            return trees
        if grid[y][x] == '.':
            pass
        elif grid[y][x] == '#':
            trees += 1
        else:
            raise Exception('unknown terrain: %s' % grid[y][x])
        location = (x, y)

assert solve(get_data('test'), PART_1_SLOPE[0], PART_1_SLOPE[1]) == PART_1_TEST
print('Part 1: %s' % solve(get_data('input'), PART_1_SLOPE[0], PART_1_SLOPE[1]))

def solve2(grid, slopes): 
    if slopes:
       slope = slopes[0]
       return solve(grid, slope[0], slope[1]) * solve2(grid, slopes[1:])
    else:
       return 1 

assert solve2(get_data('test'), PART_2_SLOPES) == PART_2_TEST
print('Part 2: %s' % solve2(get_data('input'), PART_2_SLOPES))
