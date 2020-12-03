ORIGIN = (0, 0)

def get_data(filepath):
    with open(filepath) as f:
        return [line.strip('\n') for line in f]

def solve(grid, x_speed, y_speed):
    trees = 0
    max_x = len(grid[0])
    max_y = len(grid)
    location = ORIGIN
    for line in grid:
        x = (location[0] + x_speed) % len(grid[0])
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

SLOPE = (3, 1)

assert solve(get_data('test'), SLOPE[0], SLOPE[1]) == 7
print('Part 1: %s' % solve(get_data('input'), SLOPE[0], SLOPE[1]))

def solve2(filepath): 
    grid = get_data(filepath)

    SLOPE_0 = (1, 1)
    SLOPE_1 = (3, 1)
    SLOPE_2 = (5, 1)
    SLOPE_3 = (7, 1)
    SLOPE_4 = (1, 2)
    
    return solve(grid, SLOPE_0[0], SLOPE_0[1]) * \
           solve(grid, SLOPE_1[0], SLOPE_1[1]) * \
           solve(grid, SLOPE_2[0], SLOPE_2[1]) * \
           solve(grid, SLOPE_3[0], SLOPE_3[1]) * \
           solve(grid, SLOPE_4[0], SLOPE_4[1])

assert solve2('test') == 336
print('Part 2: %s' % solve2('input'))
