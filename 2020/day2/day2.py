def is_valid(entry):
      policy, letter, password = entry.split(' ')
      letter = letter.strip(':')
      policy_lower, policy_upper = policy.split('-')
      return int(policy_lower)<=password.count(letter) and int(policy_upper)>=password.count(letter)

def part1(filepath):
    valid_passwords = 0
    entries = open(filepath).read().splitlines()
    for entry in entries:
        if is_valid(entry):
           valid_passwords+=1
    return valid_passwords

assert part1('test') == 2
print('Part 1: %s' % part1('input'))
