def countnumberswithout(n,p):
    count = 0
    res = []
    r = str(p)
    for i in range(n):
        s = str(i)
        if r not in s:
            count += 1
        else:
            res.append(int(s))
    return count,res

print(countnumberswithout(100,3))
