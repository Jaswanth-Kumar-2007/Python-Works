def subset_sum(nums,target):
    lst = [x for x in nums if x < target]
    while target not in lst:
        p = max(lst)
        target -= p
        nums.remove(p)
    else:
        if target in lst:
            return True
        else:
            return False



print(subset_sum([3,34,4,12,5,2],9))
print(subset_sum([1,2,3],7))
        



