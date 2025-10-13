def days(d,m,y):
    if (m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12):
        d += 31
    elif (m == 4 or m == 6 or m == 9 or m == 11):
        d += 30
    elif (m == 2):
        if ((y %100 == 0 and y % 4 == 0) or y%400 == 0):
            d += 29
        else:
            d += 28
    else:
        return "Invalid Month"
    if y == 0:
        d += 0
    elif ((y%100 == 0 and y%4 == 0)or y%400 == 0):
        d += 366
    else:
        d += 355

    return d

t1 = (25,2,2025)
t2 = (1,3,2025)

res = days(t1[0],t1[1],t1[2]) - days(t2[0],t2[1],t2[2])
if res > 0:
    print(res)
else:
    print(-res)

