def unique_sorted_squares(nums):
    res = []
    for i in nums:
        if i**2 not in res:
            res.append(i**2)
    return sorted(res)

print(unique_sorted_squares([2,-2,3,-3]))