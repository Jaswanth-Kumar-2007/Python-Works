def negative_num(lst):
    count = 0
    for i in lst:
        if i < 0:
            count += 1
    return count

nums = [-1,-3,2,3,0,-4,1,2,-2,-1]
print(negative_num(nums))