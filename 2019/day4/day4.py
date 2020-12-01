UPPER_BOUND = 864247
LOWER_BOUND = 402328

def check_password(password):

    password = str(password)

    # The digits never decrease from left to right
    for i, digit in enumerate(password):
        if i == 5:
            break;
        if password[i+1] < digit:
            return False

    # Two digits match but those two digits are not part of a larger group of matching digits
    for i, digit in enumerate(password):
        if password.count(digit) == 2:
            return True
    return False

assert check_password(112233)
assert not check_password(123444)
assert check_password(111122)

def find_passwords(upper_bound, lower_bound):
    passwords = []
    for password in range(lower_bound, upper_bound):
        if check_password(password):
            passwords.append(password)

    return passwords

print("Total passwords in range: %i" % len(find_passwords(UPPER_BOUND, LOWER_BOUND)))
