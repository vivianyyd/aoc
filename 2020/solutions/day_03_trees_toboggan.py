def get_trees(dx, dy, tree_map):
    """
    Find the number of trees encountered if a toboggan traverses across a map at a given slope.
    :param dx: the change in x of the slope
    :param dy: the change in y of the slope
    :param tree_map: the map, where # represents a tree
    :return: the number of trees encountered
    """
    trees, row, col = 0, 0, 0
    while row < len(tree_map):
        row += dy
        col = (col + dx) % len(tree_map[0])
        if row < len(tree_map) and tree_map[row][col] == '#':
            trees += 1
    return trees


tree_map = [line for line in open('../inputs/day_03.txt', 'r').read().split('\n') if line]
# part 1: number of trees encountered with a slope of right 3 and down 1
print(get_trees(3, 1, tree_map))
# part 2: product of number of trees encountered for each of given slopes
print(get_trees(1, 1, tree_map) * get_trees(3, 1, tree_map) * get_trees(5, 1, tree_map) * get_trees(7, 1, tree_map) * get_trees(1, 2, tree_map))
