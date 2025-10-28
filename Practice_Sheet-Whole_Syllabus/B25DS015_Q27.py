def invert_dict(d):
    res = {}
    for key,value in d.items():
        res1 = []
        for i,j in d.items():
            if d[key] == d[i]:
                res1.append(i)
            else:
                res[value] = key
        res[j] = res1
    return res

print(invert_dict({'a':1,'b':2,'d':1,'f':5}))

