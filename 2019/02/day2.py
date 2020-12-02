def parse_inputs(inputs):
    return [int(input) for input in inputs.split(',')]

def compute(inputs):
    ADD = 1
    MULTIPLY = 2
    HALT = 99
    
    i = 0
    while i < len(inputs):
        opcode = inputs[i]
        output = inputs[0]
        try:
            arg1 = inputs[inputs[i+1]]
            arg2 = inputs[inputs[i+2]]
            location = inputs[i+3]
        except IndexError:
            pass

        if opcode == ADD:
            inputs[location] = arg1 + arg2
            i += 4
        elif opcode == MULTIPLY:
            inputs[location] = arg1 * arg2
            i += 4
        elif opcode == HALT:
            return output
        else:
            raise Exception('Unrecognized opcode')

def modify_inputs(inputs, noun, verb):
    inputs = inputs.copy()
    inputs[1] = noun
    inputs[2] = verb
    return inputs

test_inputs = parse_inputs('1,9,10,3,2,3,11,0,99,30,40,50')
assert compute(test_inputs) == 3500

puzzle_inputs = parse_inputs(open('input').read())
print('Part 1: output = %i' % compute(modify_inputs(puzzle_inputs, 12, 2)))

def solve(inputs):
    TARGET = 19690720
    for noun in range(0, 99):
        for verb in range(0, 99):
            if compute(modify_inputs(inputs, noun, verb)) == TARGET:
                return 100 * noun + verb

print('Part 2: final answer = %i' % solve(puzzle_inputs))
