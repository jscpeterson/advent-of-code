def get_data(filepath):
    with open(filepath) as f:
        return [int(line) for line in f]

def part1(values):
    for v1 in values:
        for v2 in values:
            if v1+v2 == 2020:
                return v1*v2

assert part1(get_data('test')) == 514579
print(part1(get_data('input')))

def part2(values):
    for v1 in values:
        for v2 in values:
            for v3 in values:
                if v1+v2+v3 == 2020:
                    return v1*v2*v3

assert part2(get_data('test')) == 241861950
print(part2(get_data('input')))
