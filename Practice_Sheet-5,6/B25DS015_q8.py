def sort_numbers(lst):
    #Keep the Numbers in Order
    res = []
    while len(lst) != 0:
        p = lst[0]
        for i in range(len(lst)):
            if lst[i] < p:
                p = lst[i]
        res.append(p)
        lst.remove(p)
    return res

def median(numbers):
    """
    Return the statistical median of the list ’numbers’. If the listNone.
    For an odd-length list, return the middle element. For an ereturn
    the average of the two middle elements.
    """
    if numbers != []:
        nl = sort_numbers(numbers)
        p = nl
        if len(p)%2 == 0:
            return (p[int((len(p)/2)-1)]+p[int((len(p))/2)])/2
        elif len(p)%2 == 1:
            return p[int((len(p)-1)/2)]
    else:
        return None
    
#Test Cases:
#print(median([1, 2, 3])) 
#print(median([1, 2, 3, 4])) 
#print(median([])) 
#print(median([5])) 