import re

data = [line.strip('\n') for line in open('input').readlines()]

sections_that_contain = 0
sections_with_overlap = 0
for line in data:
    groups = re.match("(\d+)-(\d+),(\d+)-(\d+)", line).groups()
    first_lower_bound, first_upper_bound, second_lower_bound, second_upper_bound = (int(group) for group in groups)
    sections_that_contain += (first_lower_bound >= second_lower_bound and first_upper_bound <= second_upper_bound) or  (second_lower_bound >= first_lower_bound and second_upper_bound <= first_upper_bound)
    sections_with_overlap += first_lower_bound <= second_upper_bound and second_lower_bound <= first_upper_bound

print(f"Silver: {sections_that_contain}\nGold: {sections_with_overlap}")
