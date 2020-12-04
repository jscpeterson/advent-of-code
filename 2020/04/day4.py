import re

MISSING_FIELD = 'MISSING'

BIRTH_YEAR_PATTERN = 'byr:(\d{4})'
BIRTH_YEAR_MIN = 1920
BIRTH_YEAR_MAX = 2002
def validate_byr(passport):
    byr_re = re.search(BIRTH_YEAR_PATTERN, passport)
    if byr_re:
        byr = byr_re.group(1)
        return (BIRTH_YEAR_MIN <= int(byr) <= BIRTH_YEAR_MAX, byr)
    else:
        return (False, MISSING_FIELD)

ISSUE_YEAR_PATTERN = 'iyr:(\d{4})'
ISSUE_YEAR_MIN = 2010
ISSUE_YEAR_MAX = 2020
def validate_iyr(passport):
    iyr_re = re.search(ISSUE_YEAR_PATTERN, passport)
    if iyr_re:
        iyr = iyr_re.group(1)
        return (ISSUE_YEAR_MIN <= int(iyr) <= ISSUE_YEAR_MAX, iyr)
    else:
        return (False, MISSING_FIELD)

EXP_YEAR_PATTERN = 'eyr:(\d{4})'
EXP_YEAR_MIN = 2020
EXP_YEAR_MAX = 2030
def validate_eyr(passport):
    eyr_re = re.search(EXP_YEAR_PATTERN, passport)
    if eyr_re:
        eyr = eyr_re.group(1)
        return (EXP_YEAR_MIN <= int(eyr) <= EXP_YEAR_MAX, eyr)
    else:
        return (False, MISSING_FIELD)

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
            return ((MIN_CM <= int(hgt) <= MAX_CM), hgt+units)
        if units == 'in':
            return ((MIN_IN <= int(hgt) <= MAX_IN), hgt+units)
    else:
        return (False, MISSING_FIELD)

HCL_PATTERN = 'hcl:(#[a-z0-9]{6})'
def validate_hcl(passport):
    hcl_re = re.search(HCL_PATTERN, passport)
    if hcl_re:
        return (True, hcl_re.group(1))
    else:
        return (False, MISSING_FIELD)

ECL_PATTERN = 'ecl:(amb|blu|brn|gry|grn|hzl|oth)'
def validate_ecl(passport):
    ecl_re = re.search(ECL_PATTERN, passport)
    if ecl_re:
        return (True, ecl_re.group(1))
    else:
        return (False, MISSING_FIELD)

PID_PATTERN = 'pid:(\d+)'
PID_LENGTH = 9
def validate_pid(passport):
    pid_re = re.search(PID_PATTERN, passport)
    if pid_re:
        return (len(pid_re.group(1)) == PID_LENGTH, pid_re.group(1))
    else:
        return (False, MISSING_FIELD)

CID_PATTERN = 'cid:(\d+)'
def validate_cid(passport):
    cid_re = re.search(CID_PATTERN, passport)
    if cid_re:
        return (True, cid_re.group(1))
    else:
        return (False, MISSING_FIELD)

def parse_passport(passport_string):
    passport = {}
    for field in FIELD_VALIDATORS.keys():
        passport[field] = FIELD_VALIDATORS[field](passport_string)
    return passport

REQUIRED_FIELDS = [
    'byr',  # (Birth Year)
    'iyr',  # (Issue Year)
    'eyr',  # (Expiration Year)
    'hgt',  # (Height)
    'hcl',  # (Hair Color)
    'ecl',  # (Eye Color)
    'pid',  # (Passport ID)
]

OPTIONAL_FIELDS = [
    'cid'  # (Country ID)
]

FIELD_VALIDATORS = {
    'byr':validate_byr,  # (Birth Year)
    'iyr':validate_iyr,  # (Issue Year)
    'eyr':validate_eyr,  # (Expiration Year)
    'hgt':validate_hgt,  # (Height)
    'hcl':validate_hcl,  # (Hair Color)
    'ecl':validate_ecl,  # (Eye Color)
    'pid':validate_pid,  # (Passport ID)
    'cid':validate_cid,  # (Country ID)
}

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


def validate_passport_basic(passport_string):
    passport_fields = get_passport_fields(passport_string)
    for required_field in REQUIRED_FIELDS:
        if required_field not in passport_fields:
            return False
    return True


def validate_passport(passport_string):
    passport = parse_passport(passport_string)
    for field in passport:
        if field in REQUIRED_FIELDS and not passport[field][0]:
            return False
    return True


def solve(filepath, validation_method):
    passport_strings = get_passports(filepath)
    valid_passports = 0
    for passport_string in passport_strings:
        if validation_method(passport_string):
            valid_passports += 1
    return valid_passports


assert solve('test', validate_passport_basic) == 2
print('Part 1: %s' % solve('input', validate_passport_basic))

assert solve('test', validate_passport) == 2
print('Part 2: %s' % solve('input', validate_passport))