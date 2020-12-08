ACC = 'acc' # acc increases or decreases a single global value called the accumulator by the value given in the argument
JUMP = 'jmp' # jmp jumps to a new instruction relative to itself, the next instruction to execute is found using the argument as an offset from the jmp instruction
NO_OPERATION = 'nop' # operation immediately below is executed next
POS = '+'
NEG = '-'

def get_data(filepath):
    return [line.strip() for line in open(filepath).readlines()]

def compute(instructions, debug1 = False, debug2 = False):
    init_instructions = instructions.copy()
    accumulator = 0
    i = 0
    if debug1 or debug2:
        instructions_run = set()
    if debug2:
        instructions_changed = set()
    running = True
    while running:
        if i == len(instructions):
            return accumulator
        if debug1:
            if i in instructions_run:
                return accumulator
            else:
                instructions_run.add(i)
        if debug2:
            if i in instructions_run:
                i = 0
                accumulator = 0
                instructions = init_instructions.copy()
                instructions_run = set()
                for i2, instruction in enumerate(instructions):
                    if i2 not in instructions_changed:
                        if JUMP in instruction:
                            instructions[i2] = instruction.replace(JUMP, NO_OPERATION)
                            instructions_changed.add(i2)
                            break
                        elif NO_OPERATION in instruction:
                            instructions[i2] = instruction.replace(NO_OPERATION, JUMP)
                            instructions_changed.add(i2)
                            break
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

assert compute(get_data('test'), debug1 = True) == 5
print('Part 1: %d' % compute(get_data('input'), debug1 = True))

assert compute(get_data('test'), debug2 = True) == 8
print('Part 1: %d' % compute(get_data('input'), debug2 = True))
