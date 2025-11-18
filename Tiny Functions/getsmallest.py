def getsmallest(lst):
    p = lst[0]
    for i in lst:
        if i < p:
            p = i

    return p

print(getsmallest([28,25,42,2,28]))