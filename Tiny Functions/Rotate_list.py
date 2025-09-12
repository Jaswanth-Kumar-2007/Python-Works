def rotate_list(nums,k):
    p = len(nums)
    for i in range(k):
        s = nums[p-1]
        nums.remove(s)
        nums.insert(0,s)
    return nums

print(rotate_list([1,2,3,4,5,6],2))
print(rotate_list([1],5))
print(rotate_list([1,2,3],0))
    
        