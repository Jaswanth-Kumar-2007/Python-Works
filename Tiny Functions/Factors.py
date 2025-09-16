def factors(n):
    res = []
    for i in range(n,0,-1):
        if n%i == 0:
            res.append(i)
    res.reverse
    return res

print(factors(23))