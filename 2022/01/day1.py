import time

SOLUTION_INPUT = 'input'
ANSI_SILVER = '\033[1;37m'
ANSI_GOLD = '\033[1;33m'
ANSI_NC = '\033[0;m'

def silver(fname):
	return max([sum([int(meal) for meal in elf.split('\n')]) for elf in open(fname).read()[:-1].split('\n\n')])

def gold(fname):
	return sum(sorted([sum([int(meal) for meal in elf.split('\n')]) for elf in open(fname).read()[:-1].split('\n\n')], reverse=True)[:3])

start_time = time.time()
print('Part 1: %s%d%s' % (ANSI_SILVER, silver(SOLUTION_INPUT), ANSI_NC))
print('Solved in %s seconds' % (time.time() - start_time))
start_time = time.time()
print('Part 2: %s%d%s' % (ANSI_GOLD, gold(SOLUTION_INPUT), ANSI_NC))
print('Solved in %s seconds' % (time.time() - start_time))
