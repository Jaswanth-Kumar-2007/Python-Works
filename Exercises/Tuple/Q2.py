def tup_sort(lst):
    res = []
    while lst:
        p = lst[0]
        for j in lst:
            if j[1] < p[1]:
                p = j
        lst.remove(p)
        res.append(p)
    return res

ans = [(2,3.0),(4,1.0),(3,6.0)]

print(tup_sort(ans))
