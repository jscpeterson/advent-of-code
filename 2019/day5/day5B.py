PCODE_LEN = 2

ADD = 1
MULTIPLY = 2
SAVE = 3
OUTPUT = 4
HALT = 99

OP_PARAMS = {
    ADD: 3,
    MULTIPLY: 3,
    SAVE: 1,
    OUTPUT: 1,
    HALT: 0,
}

POSITION = 0
IMMEDIATE = 1


class IntcodeCompiler:

    def __init__(self, filepath):
        with open(filepath) as f:
            self.program = list(map(int, f.read().strip().split(',')))
            f.close()

    def read(self, position, mode):
        if mode == POSITION:
            return self.program[position]
        elif mode == IMMEDIATE:
            return position
        else:
            raise Exception('Unrecognized mode: {}'.format(mode))

    def write(self, position, input_):
        self.program[position] = input_

    def run(self, input_=None):
        instruction_pointer = 0
        output = None
        while instruction_pointer < len(self.program):
            instruction = self.program[instruction_pointer]
            opcode = instruction % 100
            # params = [parameter for parameter in self.program[instruction_pointer+1:OP_PARAMS[opcode]+1]]
            modes = instruction // 100

            if opcode == ADD:
                operand1 = self.read(self.program[instruction_pointer + 1], modes % 10)
                modes = modes // 10
                operand2 = self.read(self.program[instruction_pointer + 2], modes % 10)
                modes = modes // 10
                self.write(self.program[instruction_pointer + 3], operand1 + operand2)
            elif opcode == MULTIPLY:
                operand1 = self.read(self.program[instruction_pointer + 1], modes % 10)
                modes = modes // 10
                operand2 = self.read(self.program[instruction_pointer + 2], modes % 10)
                modes = modes // 10
                self.write(self.program[instruction_pointer + 3], operand1 * operand2)
            elif opcode == SAVE:
                self.write(self.program[instruction_pointer + 1], input_)
            elif opcode == OUTPUT:
                output = self.read(self.program[instruction_pointer + 1], modes % 10)
            elif opcode == HALT:
                return output
            else:
                raise Exception('Unrecognized opcode: {}'.format(opcode))

            instruction_pointer += 1 + OP_PARAMS[opcode]


# test_machine = IntcodeCompiler('test1')
# print(test_machine.program)
print(IntcodeCompiler('input').run(input_=1))

