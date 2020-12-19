import time

SOLUTION_INPUT = 'input'
ANSI_SILVER = '\033[1;37m'
ANSI_GOLD = '\033[1;33m'
ANSI_NC = '\033[0;m'    
DIGITS = '0123456789'
OPERATORS = '+*'
SILVER_TESTS = {'1+(2*3)+(4*(5+6))': 51,
                '2*3+(4*5)': 26,
                '5+(8*3+9+3*4*3)': 437,
                '5*9*(7*3*3+9*3+(8+6*4))': 12240,
                '((2+4*9)*(6+9*8+6)+6)+2+4*2': 13632}
GOLD_TESTS = {'1+(2*3)+(4*(5+6))': 51,
              '2*3+(4*5)': 46,
              '5+(8*3+9+3*4*3)': 1445,
              '5*9*(7*3*3+9*3+(8+6*4))': 669060,
              '((2+4*9)*(6+9*8+6)+6)+2+4*2': 23340}

def get_data(filepath):
    return [line.strip().replace(' ','') for line in open(filepath).readlines()]

def solve(calculation_method, filepath):
    expressions = get_data(filepath)
    return sum(calculation_method(expression) for expression in expressions)

def calculate_silver(expression=None, tokens=None):
    if expression and not tokens:
        tokens = [token for token in expression]
    operands = list()
    operators = list()
    while tokens:
        token = tokens.pop(0)
        if token in DIGITS:
            operands.append(int(token))
        elif token in OPERATORS:
            operators.append(token)
        elif token in '(':
            operands.append(calculate_silver(tokens=tokens))
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

def calculate_gold(expression=None, tokens=None):
    if expression and not tokens:
        tokens = [token for token in expression]
    operands = list()
    operators = list()
    while tokens:
        token = tokens.pop(0)
        if token in DIGITS:
            operands.append(int(token))
        elif token in OPERATORS:
            operators.append(token)
        elif token in '(':
            operands.append(calculate_gold(tokens=tokens))
        elif token in ')':
            break
    priority_level = 0
    while operators:
        if OPERATORS[priority_level] not in operators:
            priority_level += 1
            continue
        if OPERATORS[priority_level] == operators[0]:
            operand1 = operands.pop(0)
            operator = operators.pop(0)
            operand2 = operands.pop(0)
            if operator == '+':
                operands.insert(0, operand1+operand2)
            elif operator == '*':
                operands.insert(0, operand1*operand2)
        else:
            operands.append(operands.pop(0))
            operators.append(operators.pop(0))
    return operands[0]

def test_calculate(calculate_method, test_cases):
    return all(calculate_method(expression) == test_cases[expression] for expression in test_cases)

def results(solution_method_1, solution_method_2):
    assert test_calculate(solution_method_1, SILVER_TESTS)
    start_time = time.time()
    print('Part 1: %s%d%s' % (ANSI_SILVER, solve(solution_method_1, SOLUTION_INPUT), ANSI_NC))
    print('Solved in %s seconds' % (time.time() - start_time))
    assert test_calculate(solution_method_2, GOLD_TESTS)
    start_time = time.time()
    print('Part 2: %s%d%s' % (ANSI_GOLD, solve(solution_method_2, SOLUTION_INPUT), ANSI_NC))
    print('Solved in %s seconds' % (time.time() - start_time))

results(calculate_silver, calculate_gold)