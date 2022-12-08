import sys

def find_start_of_packet(datastream, sequence_length=4):
    for i in range(sequence_length, len(datastream)):
        subsection = datastream[i-sequence_length:i] 
        if len(set(subsection)) == sequence_length:
            return i
 
filename = sys.argv[1]

input_string = open(filename).read().strip()

print(f"Silver: {find_start_of_packet(input_string)}")
print(f"Gold: {find_start_of_packet(input_string, sequence_length=14)}")

