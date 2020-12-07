TARGET_BAG = 'shiny gold'


def get_data(filepath):
    return [line.strip() for line in open(filepath).readlines()]


def parse_rule(rule):
    rule = rule.split(' ')
    adj, color = rule[0], rule[1]
    container_bag = '%s %s' % (adj, color)
    bags_contained = {}
    if rule[4:] == ['no', 'other', 'bags.']:
        pass
    else:
        for i in range(4, len(rule), 4):
            quantity, adj, color = rule[i], rule[i + 1], rule[i + 2]
            bags_contained['%s %s' % (adj, color)] = int(quantity)
    return container_bag, bags_contained


def parse_bag_rules(inputs):
    bag_rules = {}
    for line in inputs:
        container_bag, bags_contained = parse_rule(line)
        bag_rules[container_bag] = bags_contained
    return bag_rules

def bag_contains_target(bag_rules, bag_to_search, target_bag):
    if bag_rules[bag_to_search]:
        for bag in bag_rules[bag_to_search]:
            if bag == target_bag:
                return True
            else:
                if bag_contains_target(bag_rules, bag, target_bag):
                    return True
    else:
        return False


def solve(inputs):
    bag_rules = parse_bag_rules(inputs)
    good_bags = []
    for bag in bag_rules.keys():
        if bag_contains_target(bag_rules, bag, TARGET_BAG):
            good_bags.append(bag)
    return len(good_bags)


def search_bags(bag_rules, bag_to_search, num_bags):
    num_bags_total = num_bags
    for bag in bag_rules[bag_to_search]:
        num_bags_inside = bag_rules[bag_to_search][bag]
        num_bags_total += num_bags * search_bags(bag_rules, bag, num_bags_inside)
    return num_bags_total


def solve2(inputs):
    bag_rules = parse_bag_rules(inputs)
    return search_bags(bag_rules, TARGET_BAG, 1) - 1  # Bag count does not include target bag


assert solve(get_data('test')) == 4
print('Part 1: %d' % solve(get_data('input')))

assert solve2(get_data('test')) == 32
assert solve2(get_data('test2')) == 126
print('Part 2: %d' % solve2(get_data('input')))
