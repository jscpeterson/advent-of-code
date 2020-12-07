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
    bag_rules = {}
    for line in inputs:
        container_bag, bags_contained = parse_rule(line)
        bag_rules[container_bag] = bags_contained
    good_bags = []
    for bag in bag_rules.keys():
        if bag_contains_target(bag_rules, bag, TARGET_BAG):
            good_bags.append(bag)
    return len(good_bags)


assert solve(get_data('test')) == 4
print('Part 1: %d' % solve(get_data('input')))
