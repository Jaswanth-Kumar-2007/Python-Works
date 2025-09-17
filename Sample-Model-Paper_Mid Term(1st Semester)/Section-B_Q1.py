def rotate_list(nums,k):
    for i in range(k):
        nums.insert(0,nums[len(nums)-1])
        nums.pop((len(nums)-1))
        print(nums)
    
#print(rotate_list([1,2,3,4,5],2))
rotate_list([1,2,3,4,5],2)