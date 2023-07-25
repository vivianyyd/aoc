def load_bags(input_file):
    """
    Create a tree-like structure to store bags and the number of each type of bag they may hold.
    :param input_file: the file from which info is taken
    :return: a dictionary containing all bags with structure {bag type : {sub bags : num}}
    """
    bags = {}
    with open(input_file, 'r') as f:
        for line in f:
            for remove in ' bags', ' bag', '.', '\n':
                line = line.replace(remove, '')
            curr_bag = {}
            color, contents = line.split(' contain ')
            if 'no other' not in line:
                contents = contents.split(', ')
                for sub_bag in contents:
                    curr_bag[sub_bag[2:]] = sub_bag[0]
            bags[color] = curr_bag
    return bags


def direct_parents(bags):
    """
    Create a parent dictionary from the bag tree.
    :param bags: the dictionary of bags and their contents
    :return: a dictionary containing each child bag's parent with structure {bag : [parents]}
    """
    parents = {}
    for bag in bags:
        for child in bags[bag]:
            if child not in parents:
                parents[child] = []
            parents[child].append(bag)
    return parents


def all_poss_parents(find_bag, parent_refs):
    """
    Find all bags which can eventually hold the bag of interest.
    :param find_bag: the bag of interest
    :param parent_refs: a dictionary of parent references
    :return:
    """
    parents = set()
    if find_bag not in parent_refs:  # bag with no parents (not a child)
        return set()
    parents.update(parent_refs[find_bag])
    for parent in parent_refs[find_bag]:
        parents.update(all_poss_parents(parent, parent_refs))
    return set(parents)


def count_sub_bags(top_bag, bags):
    """
    Count the number of bags the top bag must hold.
    :param top_bag: the top bag
    :param bags: the dictionary of all bags and their contents
    :return: the number of bags held by the top bag
    """
    count = 1
    for b in bags[top_bag].keys():
        count += int(bags[top_bag][b]) * count_sub_bags(b, bags)
    return count


all_bags = load_bags('../inputs/day_07.txt')
parent_ref = direct_parents(all_bags)
print(len(all_poss_parents('shiny gold', parent_ref)))
print(count_sub_bags('shiny gold', all_bags) - 1)  # exclude outermost bag
