import sys

class CPU:
   display_width = 0 
   pixel_lit = "\u2588"
   pixel_dark = " "
   cycles = 0
   x = 1
   signal_strength = 0
   signal_strengths = dict() # Cycles: signal_strength

   def __init__(self, display_width=40):    
       self.display_width = display_width

   def get_signal_strength_sums(self):
       return sum(self.signal_strengths.values())

   def update_cycles_and_display(self):       
       self.cycles += 1

       # Check signal strength
       if self.cycles == 20 or (self.cycles + 20) % 40 == 0:
           self.signal_strength = self.cycles * self.x
           self.signal_strengths[self.cycles] = self.signal_strength

       # Adjust for correct CRT row
       pixel_being_drawn = (self.cycles-1) % self.display_width
       new_line = pixel_being_drawn == 0
       if new_line:
           sys.stdout.write('\n')

       # Display pixel based on current x register
       sprite_in_x_register = (self.x-1, self.x, self.x+1)
       sys.stdout.write(self.pixel_lit) if pixel_being_drawn in sprite_in_x_register else sys.stdout.write(self.pixel_dark)

   def run(self, program_instructions):
       for instruction in program_instructions:
           # Start cycle               
           self.update_cycles_and_display()

           # Run operation
           arguments = instruction.split(' ')
           op = arguments[0]
           if op == 'noop':
               pass
           elif op == 'addx':
               self.update_cycles_and_display()
               value = arguments[1]
               self.x += int(value)
           else:
               raise Exception(f"Unrecognized operation: {op}")
 
filename = sys.argv[1]

program_instructions = [line.strip("\n") for line in open(filename).readlines()]

device = CPU()
device.run(program_instructions)
print(f"\n\nCycle strengths sum: {device.get_signal_strength_sums()}")
