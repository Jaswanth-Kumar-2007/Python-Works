def invert_dict(d):
    res = {}
    for key,value in d.items():
        res[value] = key
    return res

print(invert_dict({"a":1,"b":2}))