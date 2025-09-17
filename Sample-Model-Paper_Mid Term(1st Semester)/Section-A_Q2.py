def frequent_number(nums):
    res = []
    maxcount = 1
    for i in nums:
        count = 0
        for j in nums:
            if i == j:
                count += 1
        if count >= maxcount:
            maxcount = count
            mode = i
        if mode not in res:
            res.append(mode)
    return res

print(frequent_number([2,3,4,5,6,7,3,5,5,5,3,3,6,6,6]))
                