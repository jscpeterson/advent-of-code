from day4 import get_passports, parse_passport, validate_passport, REQUIRED_FIELDS

ANSI_RED = '\033[0;31m'
ANSI_GREEN = '\033[0;32m'
ANSI_NC = '\033[0m'


def display_passport(passport):
    display_string = ''
    for field in passport:
        display_string += '%s: %s%s%s\n' % (field, ANSI_RED if not passport[field][0] and field in REQUIRED_FIELDS else ANSI_GREEN, passport[field][1], ANSI_NC)
    return display_string


def solve_pretty(filepath, validation_method):
    passport_strings = get_passports(filepath)
    valid_passports = 0
    for i, passport_string in enumerate(passport_strings):
        passport = parse_passport(passport_string)
        print('\nPassport [%d/%d]%s' % (i, len(passport_strings), ANSI_NC))
        if validation_method(passport_string):
            valid_passports += 1
            print('%sVALID (#%d)%s' % (ANSI_GREEN, valid_passports, ANSI_NC))
        else:
            print('%sINVALID%s' % (ANSI_RED, ANSI_NC))
        print(display_passport(passport))
    return valid_passports


solve_pretty('input', validate_passport)
