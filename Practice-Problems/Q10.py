def sumnum(p):
    sum = 0
    if p == 0:
        return 0
    else:
        return p+sumnum(p-1)

print(sumnum(25))