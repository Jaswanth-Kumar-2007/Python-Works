def answer(n):
    res = []
    for a in range(n):
        for b in range(n):
            if a**2 == b**3:
                s = [a,b]
                res.append(s)
    return res,len(res)

print(answer(1000))

def answer2(n):
    res = []
    t = 1
    while len(res) != n:
        for a in range(t):
            for b in range(t):
                if a**2 == b**3:
                    r = [a,b]
                    if r not in res:
                        res.append(r)
        t += 1
    return res

print(answer2(10))
        