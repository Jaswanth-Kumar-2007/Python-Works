def majority_element(nums):
    arr= []
    n = len(nums)
    mode = 0
    res = []
    for i in nums:
        count = 0
        for j in nums:
            if i == j:
                count += 1
        if count > (n//3):
            mode = i
        if mode not in res:
            res.append(mode)
        if 0 in res:
            res.remove(0)
    
    nums = res
    print(nums)
    res1 = []
    while nums != []:
        d = nums[0]
        for i in range(len(nums)):
            if nums[i] < d:
                d = nums[i]
        res1.append(d)
        nums.remove(d)
        
    nums = res1
        
    return nums

print(majority_element([2,2,3,1,3,2,1,1]))
print(majority_element([-5,3,-5]))
print(majority_element([3,2,2,4,1,4]))
print(majority_element([15,15,15,15,13,13,13,13,15,13]))