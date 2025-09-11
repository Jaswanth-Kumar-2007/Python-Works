def poweranumber(a,b):
    res = 1
    for i in range(b):
        res *= a
    return res

print(poweranumber(7,3))