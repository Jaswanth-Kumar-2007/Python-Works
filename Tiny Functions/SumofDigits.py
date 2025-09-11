def sumofdigits(n):
    p = list(str(n))
    res = 0
    for i in p:
        res += int(i)
    return res

print(sumofdigits(234))