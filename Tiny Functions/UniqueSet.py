def unique_set(nums):
    res = []
    for i in nums:
        if i not in res:
            res.append(i)
        else:
            pass
    return res

print(unique_set([2,3,3,1,1,5,3,2,4,6,7,8,6,5,6]))