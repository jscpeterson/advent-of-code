import sys

CYCLES_TO_CHECK = [20, 60, 100, 140, 180, 220]

class CPU:
   display_width = 0
   display_height = 0
   cycles = 0
   x = 1
   signal_strength = 0
   signal_strengths = dict() # Cycles: signal_strength

   def __main__(display_width=40, display_height=6):
       pass

   def get_signal_strength_sums(self):
       return sum(self.signal_strengths.values())

   def update_cycles(self):       
       self.cycles += 1

       # Check signal strength
       if self.cycles == 20 or (self.cycles + 20) % 40 == 0:
           self.signal_strength = self.cycles * self.x
           self.signal_strengths[self.cycles] = self.signal_strength

   def run(self, program_instructions):
       for instruction in program_instructions:
           # Start cycle
           self.update_cycles()
                          
           # Run operation
           arguments = instruction.split(' ')
           op = arguments[0]
           if op == 'noop':
               pass
           elif op == 'addx':
               self.update_cycles()
               value = arguments[1]
               self.x += int(value)
           else:
               raise Exception(f"Unrecognized operation: {op}")
 
filename = sys.argv[1]

program_instructions = [line.strip("\n") for line in open(filename).readlines()]

device = CPU()
device.run(program_instructions)
print(f"Silver: {device.get_signal_strength_sums()}")
print(f"Gold: ??? ")
