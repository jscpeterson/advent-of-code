import re

BIRTH_YEAR_PATTERN = 'byr:(\d\d\d\d)'
BIRTH_YEAR_MIN = 1920
BIRTH_YEAR_MAX = 2002
def validate_byr(passport):
    byr_re = re.search(BIRTH_YEAR_PATTERN, passport)
    if byr_re:
        byr = byr_re.group(1)
        return BIRTH_YEAR_MIN <= int(byr) <= BIRTH_YEAR_MAX
    else:
        return False

ISSUE_YEAR_PATTERN = 'iyr:(\d\d\d\d)'
ISSUE_YEAR_MIN = 2010
ISSUE_YEAR_MAX = 2020
def validate_iyr(passport):
    iyr_re = re.search(ISSUE_YEAR_PATTERN, passport)
    if iyr_re:
        iyr = iyr_re.group(1)
        return ISSUE_YEAR_MIN <= int(iyr) <= ISSUE_YEAR_MAX
    else:
        return False

EXP_YEAR_PATTERN = 'eyr:(\d\d\d\d)'
EXP_YEAR_MIN = 2020
EXP_YEAR_MAX = 2030
def validate_eyr(passport):
    eyr_re = re.search(EXP_YEAR_PATTERN, passport)
    if eyr_re:
        eyr = eyr_re.group(1)
        return EXP_YEAR_MIN <= int(eyr) <= EXP_YEAR_MAX
    else:
        return False

HGT_PATTERN = 'hgt:(\d?\d\d)(in|cm)'
MIN_CM = 150
MAX_CM = 193
MIN_IN = 59
MAX_IN = 76
def validate_hgt(passport):
    hgt_re = re.search(HGT_PATTERN, passport)
    if hgt_re:
        hgt = hgt_re.group(1)
        units = hgt_re.group(2)
        if units == 'cm':
            return MIN_CM <= int(hgt) <= MAX_CM
        if units == 'in':
            return MIN_IN <= int(hgt) <= MAX_IN
    else:
        return False

HCL_PATTERN = 'hcl:(#[a-z0-9]{6})'
def validate_hcl(passport):
    return re.search(HCL_PATTERN, passport)

ECL_PATTERN = 'ecl:(amb|blu|brn|gry|grn|hzl|oth)'
def validate_ecl(passport):
    return re.search(ECL_PATTERN, passport)

PID_PATTERN = 'pid:(\d+)'
def validate_pid(passport):
    pid_re = re.search(PID_PATTERN, passport)
    if pid_re:
        return len(pid_re.group(1)) == 9

REQUIRED_FIELD_VALIDATORS = {
    'byr':validate_byr,  # (Birth Year)
    'iyr':validate_iyr,  # (Issue Year)
    'eyr':validate_eyr,  # (Expiration Year)
    'hgt':validate_hgt,  # (Height)
    'hcl':validate_hcl,  # (Hair Color)
    'ecl':validate_ecl,  # (Eye Color)
    'pid':validate_pid,  # (Passport ID)
}

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


def validate_passport_basic(passport):
    passport_fields = get_passport_fields(passport)
    for required_field in REQUIRED_FIELD_VALIDATORS.keys():
        if required_field not in passport_fields:
            return False
    return True

def validate_passport(passport):
    for required_field in REQUIRED_FIELD_VALIDATORS:
        if not REQUIRED_FIELD_VALIDATORS[required_field](passport):
            return False
    return True

def solve(filepath, validation_method):
    passports = get_passports(filepath)
    valid_passports = 0
    for passport in passports:
        if validation_method(passport):
            valid_passports += 1
    return valid_passports

assert solve('test', validate_passport_basic) == 2
print('Part 1: %s' % solve('input', validate_passport_basic))

assert solve('test', validate_passport) == 2
print('Part 2: %s' % solve('input', validate_passport))