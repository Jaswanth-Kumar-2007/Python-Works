def invert_dict(d):
    res = {}
    for key, value in d.items():
        if value not in res:
            res[value] = [key]
        else:
            res[value].append(key)
    return res

print(invert_dict({'a': 1, 'b': 2, 'd': 1, 'f': 5,'c':1}))
