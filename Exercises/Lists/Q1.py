def no_duplicate(lst):
    res = []
    for i in lst:
        if i not in res:
            res.append(i)
    return res

nums = [1,2,2,3,4,4,4,2,1,5]
print(no_duplicate(nums))
