def factors(n):
    res = []
    for i in range(1,n+1):
        if n%i == 0:
            res.append(i)
    return res

print(factors(60))