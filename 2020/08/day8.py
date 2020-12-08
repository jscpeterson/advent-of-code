ACC = 'acc' # acc increases or decreases a single global value called the accumulator by the value given in the argument
JUMP = 'jmp' # jmp jumps to a new instruction relative to itself, the next instruction to execute is found using the argument as an offset from the jmp instruction
NO_OPERATION = 'nop' # operation immediately below is executed next
POS = '+'
NEG = '-'


def get_data(filepath):
    return [line.strip() for line in open(filepath).readlines()]


class InfiniteLoopException(Exception):
    pass


def compute(instructions):
    accumulator = 0
    i = 0
    instructions_run = set()
    running = True
    while running:
        if i == len(instructions):
            return accumulator
        if i in instructions_run:
            raise InfiniteLoopException({ACC: accumulator})
        else:
            instructions_run.add(i)
        operation, argument = instructions[i].split(' ')
        sign = argument[0]
        value = int(argument[1:])
        if operation == NO_OPERATION:
            pass
        elif operation == ACC:
            accumulator = accumulator+value if sign == POS else accumulator-value
        elif operation == JUMP:
            i = i+value if sign == POS else i-value
            continue
        i += 1


def solve1(filepath):
    instructions = get_data(filepath)
    try:
        compute(instructions)
    except InfiniteLoopException as e:
        return e.args[0][ACC]


def solve2(filepath, instructions_changed=None):
    if not instructions_changed:
        instructions_changed = set()
    first_instructions = get_data(filepath)
    debugging = True
    new_instructions = first_instructions[:]
    while debugging:
        try:
            return compute(new_instructions)
        except InfiniteLoopException as e:
            new_instructions = first_instructions[:]
            for i2, instruction in enumerate(first_instructions):
                if i2 not in instructions_changed:
                    if JUMP in instruction:
                        new_instructions[i2] = instruction.replace(JUMP, NO_OPERATION)
                        instructions_changed.add(i2)
                        break
                    elif NO_OPERATION in instruction:
                        new_instructions[i2] = instruction.replace(NO_OPERATION, JUMP)
                        instructions_changed.add(i2)
                        break


assert solve1('test') == 5
print('Part 1: %d' % solve1('input'))

assert solve2('test') == 8
print('Part 1: %d' % solve2('input'))
