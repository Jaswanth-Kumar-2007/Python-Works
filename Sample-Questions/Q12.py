def two_sum(lst,tar):
    ans = []
    res = [[]]

    for i in lst:
        s = []
        for j in res:
            s.append(j+[i])
        res.extend(s)

    for p in res:
        if sum(p) == tar:
            for r in p:
                ans.append(lst.index(r))
    return ans

print(two_sum([1,2,4,6],3))


