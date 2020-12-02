from datetime import datetime

print(datetime.now())

wire1 = []
wire2 = []

ORIGIN_X = 0
ORIGIN_Y = 0
ORIGIN = (ORIGIN_X, ORIGIN_Y)

def get_wire_paths(filepath):
    wirepaths = open(filepath).read().split('\n')
    wirepaths[0] = wirepaths[0].split(',')
    wirepaths[1] = wirepaths[1].split(',')
    return wirepaths[:2]

wirepaths = get_wire_paths('input')

def build_wire(wirepath): 
    wire = set()
    lengths = {}
    starting_point = ORIGIN
    wire.add(starting_point)
    total_steps = 0
    for i in range(0, len(wirepath)):
        
        instruction = wirepath[i]
        direction = instruction[0]
        steps = int(instruction[1:])
        for step in range(steps):
            total_steps += 1
            new_point = list(starting_point)
            if direction =='R':
                new_point[0] += 1
            elif direction == 'D':
                new_point[1] -= 1
            elif direction == 'U':
                new_point[1] += 1
            elif direction == 'L':
                new_point[0] -= 1
            else:
                raise Exception('Unrecognized direction for wire path')
            wire.add(tuple(new_point))
            lengths[tuple(new_point)] = total_steps
            starting_point = new_point

    return wire, lengths

wire1, lengths1 = build_wire(wirepaths[0])
wire2, lengths2 = build_wire(wirepaths[1])

intersections = []

wire1.remove(ORIGIN)
wire2.remove(ORIGIN)

path_lengths = {}

for point1 in wire1:
        if point1 in wire2 and point1 not in intersections:
            intersections.append(point1)
            path_lengths[(point1)] = lengths1[(point1)] + lengths2[(point1)]

def manhattan(point1, point2):
    x1 = point1[0]
    y1 = point1[1]
    x2 = point2[0]
    y2 = point2[1]

    return abs(x1-x2) + abs(y1-y2)

distances = [manhattan([ORIGIN_X, ORIGIN_Y], point) for point in intersections]

print('Shortest distance from origin: %i' % min(distances))
print('Shortest wirepath: %i' % min(path_lengths.values()))
print(datetime.now())

