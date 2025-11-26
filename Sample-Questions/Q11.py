def ans(p):
    res = [[]]

    for i in p:
        tr = []
        for s in res:
            tr.append(s+[i])
        res.extend(tr)
    return res

    

print(ans([1,2,3]))