def sum_target(n,k):
    res = [[]]
    for i in n:
        s = []
        for j in res:
            s.append(j+[i])
        res.extend(s)
    for i in res:
        if sum(i) == k:
            return i

print(sum_target([1,4,2,3,5,6],7))