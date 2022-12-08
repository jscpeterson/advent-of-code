import sys

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

# Returns true if a point is a valid point in a grid based on the max values (no wrapping)
def is_point_in_grid(point, max_x, max_y):
    x, y = point
    return x < max_x and x >= 0 and y < max_y and y >= 0

# Returns boolean, int - True if the tree in the grid is blocked in visibility, and the scenic score of the tree 
def get_visibility(grid, point, max_x, max_y): 
    height_at_point = grid[point]
    directions_blocked = dict()
    scenic_score = 1
    for direction in CARDINAL_DIRECTIONS:
        visible_trees = 0
        directions_blocked[direction] = False
        next_point = (point[0] + direction[0], point[1] + direction[1])
        while is_point_in_grid(next_point, max_x, max_y):
            height_at_tree_in_direction = grid[next_point]
            visibility_is_blocked = height_at_tree_in_direction >= height_at_point
            visible_trees += 1
            if visibility_is_blocked:
                directions_blocked[direction] = True
                break
            next_point = (next_point[0] + direction[0], next_point[1] + direction[1])
        scenic_score *= visible_trees
    return all(directions_blocked[key] for key in directions_blocked.keys()), scenic_score

# Shows visible trees in green
def print_grid(grid, max_x, max_y):
    for y in range(0, max_y):
        for x in range(0, max_x):
            output = grid[(x,y)]
            if (x,y) in visible_points:
                output = f"{ANSI_GREEN}{output}{ANSI_NC}"
            sys.stdout.write(output)
        sys.stdout.write('\n')

# Get data from filename argument
filename = sys.argv[1]
data = [line.strip('\n') for line in open(filename).readlines()]

# Build grid
height_grid = dict()
max_y = len(data)
max_x = len(data[0])
for y, row in enumerate(data):
    for x, height in enumerate(row):
        point = (x, y)
        height_grid[point] = height

# Check each point in grid for visibility, scenic score
visible_points = []
scenic_scores = []
for point in height_grid:
    tree_on_edge = point[0] in (0, max_x) or point[1] in (0, max_y)
    visibility_blocked, scenic_score = get_visibility(height_grid, point, max_x, max_y)
    if tree_on_edge or not visibility_blocked:
        visible_points.append(point)
    scenic_scores.append(scenic_score)

# Display grid
print_grid(height_grid, max_x, max_y)

print(f"Part 1: Number of visible points: {len(visible_points)}")
print(f"Part 2: Maximum scenic score: {max(scenic_scores)}")
