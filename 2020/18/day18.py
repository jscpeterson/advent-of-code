import time

TEST_DATA = 'test'
SOLUTION_INPUT = 'input'
ANSI_SILVER = '\033[1;37m'
ANSI_GOLD = '\033[1;33m'
ANSI_NC = '\033[0;m'    
DIGITS = '0123456789'
OPERATORS = '*+'

def get_data(filepath):
    return [line.strip().replace(' ','') for line in open(filepath).readlines()]

def silver(filepath):
    expressions = get_data(filepath)
    return sum(calculate(expression) for expression in expressions)

def calculate(expression=None, tokens=None):
    if not tokens:
        tokens = [token for token in expression]
    operands = list()
    operators = list()
    result = 0
    while tokens:
        token = tokens.pop(0)
        if token in DIGITS:
            operands.append(int(token))
        elif token in OPERATORS:
            operators.append(token)
        elif token in '(':
            operands.append(calculate(tokens=tokens))
        elif token in ')':
            break
    while operators:
        operand1 = operands.pop(0)
        operator = operators.pop(0)
        operand2 = operands.pop(0)
        if operator == '+':
            operands.insert(0, operand1+operand2)
        elif operator == '*':
            operands.insert(0, operand1*operand2)
    return operands[0]

def test_calculate():
    return calculate('2*3+(4*5)') == 26 and \
    calculate('5+(8*3+9+3*4*3)') == 437 and \
    calculate('5*9*(7*3*3+9*3+(8+6*4))') == 12240 and \
    calculate('((2+4*9)*(6+9*8+6)+6)+2+4*2') == 13632

def solve(solution_method_1, solution_method_2):
    assert test_calculate()
    start_time = time.time()
    print('Part 1: %s%d%s' % (ANSI_SILVER, solution_method_1(SOLUTION_INPUT), ANSI_NC))
    print('Solved in %s seconds' % (time.time() - start_time))
    #start_time = time.time()
    #print('Part 2: %s%d%s' % (ANSI_GOLD, solution_method_2(SOLUTION_INPUT), ANSI_NC))
    #print('Solved in %s seconds' % (time.time() - start_time))

solve(silver, None)
