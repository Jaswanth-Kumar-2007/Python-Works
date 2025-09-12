def unique_set(nums):
    # Removes the Repeated Elements
    res = []
    for i in nums:
        if i not in res:
            res.append(i)
        else:
            pass
    return res


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

def largest_unique_subarray(s):
    '''
    Return the length of the longest contiguous subarray
    of ’nums’ inelements are distinct.
    '''
    z = unique_set(s)
    y = sort_numbers(z)
    l = len(y)
    sample = []
    i = y[0]
    p = 0
    while  sample != y and  p < l:
        sample.append(i)
        i += 1
        p += 1
    if sample == y:
        return p
    else:
        return "No Longest Subbarray"


#Test Cases:    
#print(largest_unique_subarray([5, 1, 3, 5, 2, 3, 4, 1]))
#print(largest_unique_subarray([ 1,2,3,4]))
#print(largest_unique_subarray([1,1,1,1]))
#print(largest_unique_subarray([2,3,4,7]))