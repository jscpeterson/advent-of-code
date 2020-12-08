import time

ACC = 'acc' # acc increases or decreases a single global value called the accumulator by the value given in the argument
JUMP = 'jmp' # jmp jumps to a new instruction relative to itself, the next instruction to execute is found using the argument as an offset from the jmp instruction
NO_OPERATION = 'nop' # operation immediately below is executed next
POS = '+'
NEG = '-'
HISTORY = 'his'


def get_data(filepath):
    return [line.strip() for line in open(filepath).readlines()]


class InfiniteLoopException(Exception):
    def __init__(self, *args):
        self.accumulator = args[0][ACC]
        self.history = args[0][HISTORY]


def compute(instructions):
    accumulator = 0
    pointer = 0
    instructions_run = set()
    running = True
    while running:
        if pointer == len(instructions):
            return accumulator
        if pointer in instructions_run:
            raise InfiniteLoopException({ACC: accumulator, HISTORY: instructions_run})
        else:
            instructions_run.add(pointer)
        operation, argument = instructions[pointer].split(' ')
        sign = argument[0]
        value = int(argument[1:])
        if operation == NO_OPERATION:
            pass
        elif operation == ACC:
            accumulator = accumulator+value if sign == POS else accumulator-value
        elif operation == JUMP:
            pointer = pointer+value if sign == POS else pointer-value
            continue
        pointer += 1


def solve1(filepath):
    instructions = get_data(filepath)
    try:
        compute(instructions)
    except InfiniteLoopException as e:
        return e.accumulator


def solve2(filepath):
    first_instructions = get_data(filepath)
    new_instructions = first_instructions[:]
    instructions_changed = set()
    debugging = True
    while debugging:
        try:
            return compute(new_instructions)
        except InfiniteLoopException as e:
            new_instructions = first_instructions[:]
            for index, instruction in enumerate(first_instructions):
                if index in e.history and index not in instructions_changed:
                    if JUMP in instruction:
                        new_instructions[index] = instruction.replace(JUMP, NO_OPERATION)
                        instructions_changed.add(index)
                        break
                    elif NO_OPERATION in instruction:
                        new_instructions[index] = instruction.replace(NO_OPERATION, JUMP)
                        instructions_changed.add(index)
                        break


assert solve1('test') == 5
start_time = time.time()
print('Part 1: %d' % solve1('input'))
print('Solved in %s seconds' % (time.time() - start_time))

assert solve2('test') == 8
start_time = time.time()
print('Part 1: %d' % solve2('input'))
print('Solved in %s seconds' % (time.time() - start_time))