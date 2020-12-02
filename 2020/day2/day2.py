def is_valid1(entry):
      policy, letter, password = entry.split(' ')
      letter = letter.strip(':')
      policy_lower, policy_upper = policy.split('-')
      return int(policy_lower)<=password.count(letter) and int(policy_upper)>=password.count(letter)

def solve(filepath, validation_method):
    valid_passwords = 0
    entries = open(filepath).read().splitlines()
    for entry in entries:
        if validation_method(entry):
           valid_passwords+=1
    return valid_passwords

assert solve('test', is_valid1) == 2
print('Part 1: %s' % solve('input', is_valid1))

def is_valid2(entry):
      policy, letter, password = entry.split(' ')
      letter = letter.strip(':')
      policy_index1, policy_index2 = policy.split('-')
      return (password[int(policy_index1)-1] == letter) ^ (password[int(policy_index2)-1] == letter)

assert solve('test', is_valid2) == 1
print('Part 2: %s' % solve('input', is_valid2))
