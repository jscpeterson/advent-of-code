data = [line.strip('\n') for line in open('input').readlines()]

def does_contain(range1, range2):
    return all(section in range2 for section in range1)
 
def any_contain(range1, range2):
    return any(section in range2 for section in range1)

silver = 0
gold = 0
for line in data:
    assignments = line.split(',')
    ass_ranges = []
    for assignment in assignments:
        (lower_bound, upper_bound) = [int(bound) for bound in assignment.split('-')]
        ass_ranges.append(range(lower_bound, upper_bound+1))
    (ass_range1, ass_range2) = ass_ranges
    does_cont = does_contain(ass_range1, ass_range2) or does_contain(ass_range2, ass_range1)
    any_cont = any_contain(ass_range1, ass_range2)
    if does_cont:
        silver += 1
    if any_cont:
        gold += 1
print(f"Silver: {silver}\nGold: {gold}")
