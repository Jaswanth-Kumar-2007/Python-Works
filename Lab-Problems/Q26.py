def remove_consecutive_duplicates(lst):
    res = []
    while lst:
        p = lst[0]
        i = 1
        while i < len(lst) and p == lst[i]:
            lst.pop(i)  
        res.append(p)
        lst.pop(0)
    return res

print(remove_consecutive_duplicates([1,2,2,2,2,2,2,2,2,3,3,3,3]))

