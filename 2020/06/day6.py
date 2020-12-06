def solve1(filepath):
    inputs = [line.replace('\n','') for line in open(filepath).read().split('\n\n')]
    count = 0
    for answers in inputs:
        count += len(set(answers))
    return count


def solve2(filepath):
    groups = open(filepath).read().split('\n\n')
    count = 0
    for group in groups:
        responses = group.split('\n')
        answers = (set(responses[0]))
        for response in responses[1:]:
             answers = set(response).intersection(answers)
        count += len(answers)
    return count

assert solve1('test') == 11
print('Part 1: %s' % solve1('input'))

assert solve2('test') == 6
print('Part 2: %s' % solve2('input'))
