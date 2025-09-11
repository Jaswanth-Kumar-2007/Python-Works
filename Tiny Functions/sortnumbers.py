def sort_numbers(lst):
    res = []
    while len(lst) != 0:
        p = lst[0]
        for i in range(len(lst)):
            if lst[i] < p:
                p = lst[i]
        res.append(p)
        lst.remove(p)
    return res

print(sort_numbers([1,4,3,7,6,8,9,7,6,4,4,24]))
