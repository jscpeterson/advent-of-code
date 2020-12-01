# Helper functions for Advent of Code problems

def get_data(filepath):
    """Returns array of values from an input file"""
    values = []
    with open(filepath) as f:
        for line in f:
            values.append(line)
        else:
            f.close()
            return values

def test(test_cases, function):
    """Given a dictionary of test_cases containing inputs and their expected results after a function has
    been run on them, returns True if all passed, returns False if any fail with a print statement on 
    each failure."""
    successful = True
    for test_case in test_cases:
        output = function(test_case)
        if output == test_cases[test_case]:
            continue
        else:
            print('FAIL: expected {answer} for input {test_case}, got {result}'.format(
                answer=test_cases[test_case], 
                test_case=test_case, 
                output=output
            ))
            successful = False
    return successful

