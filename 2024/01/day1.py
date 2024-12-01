import time
import re
import sys

ANSI_SILVER = '\033[1;37m'
ANSI_GOLD = '\033[1;33m'
ANSI_NC = '\033[0;m'

def silver(fname):
     lines = open(fname).readlines()
     loc_sets = [line.split() for line in lines]
     col1 = [loc_set[0] for loc_set in loc_sets]
     col1.sort()
     col2 = [loc_set[1] for loc_set in loc_sets]
     col2.sort()
     distances = []
     for i in range(len(lines)):
          distances.append(abs(int(col1[i])-int(col2[i])))
     return sum(distances)

def gold(fname): 
     lines = open(fname).readlines()
     loc_sets = [line.split() for line in lines]
     col1 = [loc_set[0] for loc_set in loc_sets]
     col2 = [loc_set[1] for loc_set in loc_sets]
     similarity_score = 0
     for num1 in col1:
          similarity_score += int(num1)*col2.count(num1)
     return similarity_score

start_time = time.time()
filename = sys.argv[1]
print('Part 1: %s%d%s' % (ANSI_SILVER, silver(filename), ANSI_NC))
print('Solved in %s seconds' % (time.time() - start_time))
start_time = time.time()
print('Part 2: %s%d%s' % (ANSI_GOLD, gold(filename), ANSI_NC))
print('Solved in %s seconds' % (time.time() - start_time))
