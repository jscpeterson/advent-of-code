class IntcodeCompiler:

    ADD = 1
    MULTIPLY = 2
    SAVE = 3
    OUTPUT = 4
    JUMP_IF_TRUE = 5
    JUMP_IF_FALSE = 6
    LESS_THAN = 7
    EQUALS = 8
    ADJUST_REL = 9
    HALT = 99

    OP_PARAMS = {
        ADD: 3,
        MULTIPLY: 3,
        SAVE: 1,
        OUTPUT: 1,
        JUMP_IF_TRUE: 2,
        JUMP_IF_FALSE: 2,
        LESS_THAN: 3,
        EQUALS: 3,
        ADJUST_REL: 1,
        HALT: 0,
     }

    POSITION = 0
    IMMEDIATE = 1
    RELATIVE = 2

    relative_base = 0

    def __init__(self, filepath):
        with open(filepath) as f:
            self.program = list(map(int, f.read().strip().split(',')))
            f.close()

    def read(self, position, mode):
        position = position % len(self.program)
        if mode == self.POSITION:
	    return self.program[position]
        elif mode == self.IMMEDIATE:
	    return position
        elif mode == self.RELATIVE:
	    return self.program[position] + self.relative_base
        else:
	    raise Exception('Unrecognized mode: {}'.format(mode))

    def write(self, position, input_):
        position = position % len(self.program)
        self.program[position] = input_

    def run(self, input_=None):
        instruction_pointer = 0
        output = None
        while True:
            if instruction_pointer > len(self.program):
                instruction_pointer = instruction_pointer % len(self.program)
            instruction = self.program[instruction_pointer]
            opcode = instruction % 100
            modes = instruction // 100

            if opcode == self.ADD:
                operand1 = self.read(self.program[instruction_pointer + 1], modes % 10)
                modes = modes // 10
                operand2 = self.read(self.program[instruction_pointer + 2], modes % 10)
                modes = modes // 10
                self.write(self.program[instruction_pointer + 3], operand1 + operand2)
            elif opcode == self.MULTIPLY:
                operand1 = self.read(self.program[instruction_pointer + 1], modes % 10)
                modes = modes // 10
                operand2 = self.read(self.program[instruction_pointer + 2], modes % 10)
                modes = modes // 10
                self.write(self.program[instruction_pointer + 3], operand1 * operand2)
            elif opcode == self.SAVE:
                self.write(self.program[instruction_pointer + 1], input_)
            elif opcode == self.OUTPUT:
                output = self.read(self.program[instruction_pointer + 1], modes % 10)
                print(output)
            elif opcode == self.JUMP_IF_TRUE:
                if self.read(self.program[instruction_pointer + 1], modes % 10) == 1:
                    modes = modes // 10
                    instruction_pointer = self.read(self.program[instruction_pointer + 2], modes % 10)
                    continue
            elif opcode == self.JUMP_IF_FALSE:
                if self.read(self.program[instruction_pointer + 1], modes % 10) == 0:
                    modes = modes // 10
                    instruction_pointer = self.read(self.program[instruction_pointer + 2], modes % 10)
                    continue
            elif opcode == self.LESS_THAN:
                operand1 = self.read(self.program[instruction_pointer + 1], modes % 10)
                modes = modes // 10
                operand2 = self.read(self.program[instruction_pointer + 2], modes % 10)
                modes = modes // 10
                self.write(self.program[instruction_pointer + 3], 1 if operand1 < operand2 else 0)
            elif opcode == self.EQUALS:
                operand1 = self.read(self.program[instruction_pointer + 1], modes % 10)
                modes = modes // 10
                operand2 = self.read(self.program[instruction_pointer + 2], modes % 10)
                modes = modes // 10
                self.write(self.program[instruction_pointer + 3], 1 if operand1 == operand2 else 0) 
            elif opcode == self.ADJUST_REL:
                self.relative_base += self.program[instruction_pointer + 1]
            elif opcode == self.HALT:
                return output
            else:
                raise Exception('Unrecognized opcode: {}'.format(opcode))

            instruction_pointer += 1 + self.OP_PARAMS[opcode]

# assert IntcodeCompiler('test1').run(input_=1) == 999
# assert IntcodeCompiler('test1').run(input_=8) == 1000
# assert IntcodeCompiler('test1').run(input_=9) == 1001
#print(IntcodeCompiler('input').run(input_=5))
print(IntcodeCompiler('test2').run())
print(IntcodeCompiler('test3').run())
print(IntcodeCompiler('test4').run())
print(IntcodeCompiler('input').run(1))
