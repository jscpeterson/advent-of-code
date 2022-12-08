import sys
from numpy import prod as product

filename = sys.argv[1]

ANSI_GREEN = '\033[0;32m'
ANSI_NC = '\033[0;m'

CARDINAL_DIRECTIONS = [
  (0, -1), #north
#  (1, -1), #northeast
  (1, 0), #east
#  (1, 1), #southeast
  (0, 1), #south
#  (-1, 1), #southwest
  (-1, 0), #west
#  (-1, -1) #northwest
]

data = [line.strip('\n') for line in open(filename).readlines()]

def point_in_grid(point, max_x, max_y):
    x, y = point
    return x < max_x and x >= 0 and y < max_y and y >= 0

# Build grid
grid = dict()
max_y = len(data)
max_x = len(data[0])
all_neighbors = dict()
for y, row in enumerate(data):
    for x, height in enumerate(row):
        point = (x, y)
        neighbors = []
        for possible_neighbor in CARDINAL_DIRECTIONS:
            neighbor_x = x + possible_neighbor[0]
            neighbor_y = y + possible_neighbor[1]
            neighbor = (neighbor_x, neighbor_y)
            if point_in_grid(neighbor, max_x, max_y):
                neighbors.append(neighbor)
        all_neighbors[point] = neighbors
        grid[point] = height

def is_visibility_blocked(grid, point, max_x, max_y): 
    height_at_point = grid[point]
    directions_blocked = dict()
    scenic_score = 1
    for direction in CARDINAL_DIRECTIONS:
        visible_trees = 0
        directions_blocked[direction] = False
        next_point = (point[0] + direction[0], point[1] + direction[1])
        while point_in_grid(next_point, max_x, max_y):
            height_at_tree_in_direction = grid[next_point]
            visibility_is_blocked = height_at_tree_in_direction >= height_at_point
            visible_trees += 1
            if visibility_is_blocked:
                print(f"Point {point} with height {height_at_point} BLOCKED by {next_point} with height {height_at_tree_in_direction}")
                directions_blocked[direction] = True
                break
            next_point = (next_point[0] + direction[0], next_point[1] + direction[1])
        scenic_score *= visible_trees
    return all(directions_blocked[key] for key in directions_blocked.keys()), scenic_score

visible_points = []
scenic_scores = []
for point in grid:
    neighboring_trees = all_neighbors[point]
    tree_on_edge = len(neighboring_trees) < len(CARDINAL_DIRECTIONS)
#    is_visible_tree = any(grid[neighboring_tree_position] < height_at_point for neighboring_tree_position in all_neighbors[point])
#    if is_tree_on_edge or is_visible_tree:
#        visible_points.append(point)     

    visibility_blocked, scenic_score = is_visibility_blocked(grid, point, max_x, max_y)
    if tree_on_edge or not visibility_blocked:
        visible_points.append(point)
    scenic_scores.append(scenic_score)

def print_grid(grid, max_x, max_y):
    for y in range(0, max_y):
        for x in range(0, max_x):
            output = grid[(x,y)]
            if (x,y) in visible_points:
                output = f"{ANSI_GREEN}{output}{ANSI_NC}"
            sys.stdout.write(output)

        sys.stdout.write('\n')

print_grid(grid, max_x, max_y)

print(len(visible_points))
print(f"Part 2: {max(scenic_scores)}")
