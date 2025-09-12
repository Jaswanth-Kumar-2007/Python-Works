def unique_set(nums):
    res = []
    for i in nums:
        if i not in res:
            res.append(i)
        else:
            pass
    return res


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

def largest_unique_subarray(s):
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
    
print(largest_unique_subarray([5, 1, 3, 5, 2, 3, 4, 1]))