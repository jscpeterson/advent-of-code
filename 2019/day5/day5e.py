
OPCODE_LEN = 2

ADD = '01'
MULTIPLY = '02'
SAVE = '03'
OUTPUT = '04'
HALT = '99'

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
            self.program = f.read().strip().split(',')
            f.close()

    def read(self, position, mode):
        if mode == POSITION:
            return int(self.program[position])
        elif mode == IMMEDIATE:
            return position
        else:
            raise Exception('Unrecognized mode: {}'.format(mode))

    def write(self, position, input_):
        print(position)
        print(input_)
        self.program[position] = input_

    def run(self, input_ = None):
        instruction_index = 0
        while instruction_index < range(0, len(self.program)):
            instruction = str(self.program[instruction_index])
            opcode = instruction.zfill(OPCODE_LEN)[-OPCODE_LEN:]
            params = [int(parameter) for parameter in self.program[instruction_index+1:OP_PARAMS[opcode]+1]]
            modes = [int(mode) for mode in instruction[:-OPCODE_LEN].zfill(OP_PARAMS[opcode])]

            if opcode == ADD:
                operand1 = self.read(params[0], modes[0])
                operand2 = self.read(params[1], modes[1])
                self.write(params[2], operand1 + operand2)
            elif opcode == MULTIPLY:
                operand1 = self.read(params[0], modes[0])
                operand2 = self.read(params[1], modes[1])
                self.write(params[2], operand1 * operand2)
            elif opcode == SAVE:
                self.write(params[0], input_)
            elif opcode == OUTPUT:
                return self.read(params[0], modes[0])
            elif opcode == HALT:
                return
            else:
                raise Exception('Unrecognized mode: {}'.format(mode))

            instruction_index += OP_PARAMS[opcode] + 1
               
test_machine = IntcodeCompiler('input')
print(test_machine.program)
print(test_machine.run(input_=1))
