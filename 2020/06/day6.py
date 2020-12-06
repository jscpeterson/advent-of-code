def solve1(filepath):
    inputs = [line.replace('\n','') for line in open(filepath).read().split('\n\n')]
    count = 0
    for answers in inputs:
        count += len(set(answers))
    return count


ANSI_RED = '\033[0;31m'
ANSI_GREEN = '\033[0;32m'
ANSI_NC = '\033[0m'

def display_group(i, groups_len, count, group, answers):
    group_string = 'Group %d/%d\n' % (i+1, groups_len)
    for c in group:
        group_string+='%s%s%s' % (ANSI_GREEN if c in answers else ANSI_RED, c, ANSI_NC)
    group_string+='\nAnswers: %s\nSum: %d Total: %d\n' % (','.join(answers), len(answers), count)
    return group_string


def solve2(filepath, pretty=False):
    groups = [line.strip() for line in open(filepath).read().split('\n\n')]
    count = 0
    for i, group in enumerate(groups):
        responses = group.split('\n')
        answers = (set(responses[0]))
        for response in responses[1:]:
             answers = set(response).intersection(answers)
        count += len(answers)
        if pretty:
             print(display_group(i, len(groups), count, group, answers))
    return count

assert solve1('test') == 11
print('Part 1: %s' % solve1('input'))

assert solve2('test') == 6
print('Part 2: %s' % solve2('input'))
