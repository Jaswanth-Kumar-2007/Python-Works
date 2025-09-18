def max_number(arr):
    maxnumber = 0
    for i in arr:
        if i > maxnumber:
            maxnumber = i
    while maxnumber in arr:
        arr.remove(maxnumber)
    if arr != []:
        maxnumber2 = 0
        for r in arr:
            if r > maxnumber2:
                maxnumber2 = r
        return maxnumber2
    else:
        return -1
    

print(max_number([12, 35,35, 1, 10, 34, 1]))
    