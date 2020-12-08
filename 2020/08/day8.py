ACC = 'acc' # acc increases or decreases a single global value called the accumulator by the value given in the argument
JUMP = 'jmp' # jmp jumps to a new instruction relative to itself, the next instruction to execute is found using the argument as an offset from the jmp instruction
NO_OPERATION = 'nop' # operation immediately below is executed next
POS = '+'
NEG = '-'

def get_data(filepath):
    return [line.strip() for line in open(filepath).readlines()]

def compute(instructions, debug = False):
    accumulator = 0
    i = 0
    if debug:
        instructions_run = set()
    running = True
    while running:
        if debug:
            if i in instructions_run:
                return accumulator
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

assert compute(get_data('test'), debug = True) == 5
print('Part 1: %d' % compute(get_data('input'), debug = True))
