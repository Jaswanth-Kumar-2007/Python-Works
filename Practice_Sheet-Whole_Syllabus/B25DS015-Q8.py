def get_odd_indices(items):
    l = len(items)
    res = []
    for i in range(1,l,2):
        res.append(items[i])
    return res

print(get_odd_indices([10,20,30,40,50]))