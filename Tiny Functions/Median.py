def sort_numbers(lst):
    res = []
    while len(lst) != 0:
        p = lst[0]
        for i in range(len(lst)):
            if lst[i] < p:
                p = lst[i]
        res.append(p)
        lst.remove(p)
    return res

def median(lst):
    nl = sort_numbers(lst)
    p = nl
    if len(p)%2 == 0:
        return (p[int((len(p)/2)-1)]+p[int((len(p))/2)])/2
    elif len(p)%2 == 1:
        return p[int((len(p)-1)/2)]
    else:
        return "Median Does Not Exist"
    
print(median([1,6,2,4]))