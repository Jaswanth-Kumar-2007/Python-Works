def sort_digits(lst):
    '''
    Return an integer whose decimal digits are sorted
    in ascending or Leading zeros are naturally dropped
    when converting the sorted into an integer.
    '''
    l = list(str(lst))
    res = []
    while len(l) != 0:
        p = l[0]
        for i in range(len(l)):
            if l[i] < p:
                p = l[i]
        res.append(p)
        l.remove(p)
    return int("".join(res))

#Test Cases:
#print(sort_digits(1432))
#print(sort_digits(9821388))
