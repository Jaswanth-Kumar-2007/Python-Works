def rotate_list(nums,k):
    '''
    Rotate the list ’nums’ to the right by k steps,
    modifying the list without creating a new list.
    Return the rotated list.
    '''
    p = len(nums)
    for i in range(k):
        s = nums[p-1]
        nums.remove(s)
        nums.insert(0,s)
    return nums

#Test Cases:
#print(rotate_list([1,2,3,4,5,6],6))
#print(rotate_list([1],5))
#print(rotate_list([1,2,3],0))
    
        