def ans(p):
    res = [[]]

    for i in p:
        tr = []
        for s in res:
            tr.append(s+[i])
        