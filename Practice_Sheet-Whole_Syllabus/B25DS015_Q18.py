def subset_sum(nums,target):
    for i in range(2**len(nums)):
        s= 0
        k = i
        for j in range(len(nums)):
            if k<<1:
                s += nums[len(nums)-j-1]
    
    if s == target:
        return True
    else:
        return False

print(subset_sum([3,34,4,12,5,2],9))