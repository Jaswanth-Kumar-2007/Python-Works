def finance(p,t,r):
    si = (p*t*r)/100
    ta = p + si
    return f"{ta:.2f}"

print(finance(3,4,5))
