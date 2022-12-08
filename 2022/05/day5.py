import sys
import re

filename = sys.argv[1]

# Split incoming data into drawing and instructions by blankline
drawing, instructions = [data_section.split('\n') for data_section in open(filename).read().split('\n\n')]

# Get number of container stacks from last row in drawing length
num_container_stacks = len(re.split("\s+", drawing[-1].strip()))

# Initialize list of stacks
stacks1 = [] # For solution 1 (silver)
stacks2 = [] # For solution 2 (gold)
for i in range(num_container_stacks):
    stacks1.append(list())
    stacks2.append(list())

# Arrange container stacks
for line in drawing[:-1]:
    print(line)
    containers = re.findall("(\[[A-Z]\]|\s{4})", line) # capture all "container" objects or vacant spots
    containers = [container.replace('[','').replace(']','').replace(' ','') for container in containers] # clean up whitespace and brackets
    for i, container in enumerate(containers):
        if container:
            # We are going down in the stack of containers, so we want to insert at the bottom (0)
            stacks1[i].insert(0, container)
            stacks2[i].insert(0, container)

# Read instructions
for line in instructions:
     if not line:
         continue
     num_containers_to_move, source, destination = [int(group) for group in re.match("move (\d+) from (\d+) to (\d+)", line).groups()]
     for _ in range(num_containers_to_move):
         container = stacks1[source-1].pop()
         stacks1[destination-1].append(container)

final_result = ""
for stack in stacks1:
    final_result += stack[-1]

print(f"Silver: {final_result}")

# New instructions
for line in instructions:
     if not line:
         continue
     num_containers_to_move, source, destination = [int(group) for group in re.match("move (\d+) from (\d+) to (\d+)", line).groups()]
     containers_to_move = []
     for _ in range(num_containers_to_move):
         containers_to_move.insert(0, (stacks2[source-1].pop()))
     stacks2[destination-1] += containers_to_move

final_result = ""
for stack in stacks2:
    final_result += stack[-1]

print(f"Gold: {final_result}")
