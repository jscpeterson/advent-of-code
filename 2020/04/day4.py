import re

REQUIRED_FIELDS = [
    'byr',  # (Birth Year)
    'iyr',  # (Issue Year)
    'eyr',  # (Expiration Year)
    'hgt',  # (Height)
    'hcl',  # (Hair Color)
    'ecl',  # (Eye Color)
    'pid'  # (Passport ID)
]

OPTIONAL_FIELDS = [
    'cid'  # (Country ID)
]


def get_passports(filepath):
    passports = []
    with open(filepath) as f:
        passport = ''
        for line in f.read().split('\n'):
            if line == '':
                passports.append(passport)
                passport = ''
            else:
                passport += line
    return passports


def get_passport_fields(passport):
    passport_fields = re.findall(r"(\w\w\w):", passport)
    return passport_fields


def validate_passport(passport):
    passport_fields = get_passport_fields(passport)
    for required_field in REQUIRED_FIELDS:
        if required_field not in passport_fields:
            return False
    return True

def solve(filepath):
    passports = get_passports(filepath)
    valid_passports = 0
    for passport in passports:
        if validate_passport(passport):
            valid_passports += 1
    return valid_passports

assert solve('test') == 2
print('Part 1: %s' % solve('input'))

