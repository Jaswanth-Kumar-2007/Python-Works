def tupcapital(tup):
    lst2 = []
    for i in tup:
        lst1 = []
        lst1.append(i[0])
        s = i[1]
        s1 = s[0:1].upper() + s[1:]
        lst1.append(s1)
        tup2 = tuple(lst1)
        lst2.append(tup2)
    tup3 = tuple(lst2)
    return tup3

tup = (("anna","akka"),("bammma","Banandham"))

print(tupcapital(tup))

        