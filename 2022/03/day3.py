from string import ascii_lowercase as ab

# get rucksacks
rucksacks = [line.strip('\n') for line in open('input').readlines()]

total = 0
for rucksack in rucksacks:
    l = len(rucksack)
    midpoint = int(l/2)
    compartments = (rucksack[midpoint:], rucksack[:midpoint])
    common_item = next(iter(set(compartments[0]).intersection(compartments[1])))
    priority_score = ab.find(common_item.lower())+1
    priority_score = priority_score+26 if common_item.isupper() else priority_score
    total += priority_score

print(f"Silver: {total}")

total = 0
groups = [rucksacks[i:i+3] for i in range(0, len(rucksacks), 3)]
for group in groups:
    common_item = next(iter(set(group[0]).intersection(group[1], group[2])))
    priority_score = ab.find(common_item.lower())+1
    priority_score = priority_score+26 if common_item.isupper() else priority_score
    total += priority_score

print(f"Gold: {total}")
