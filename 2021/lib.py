def add(dic, k, v):
    """ Sets dic[k] to dic[k] + v, or v if k is not in dic. """
    if k in dic:
        dic[k] += v
    else:
        dic[k] = v
