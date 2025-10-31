def subset_sum(nums,target):
    if target == 0:
        return True
    if not nums:
        return False
    n = nums[0]
    include = subset_sum(nums[1:],target-n)
    exclude = subset_sum(nums[1:],target)
    return include or exclude

print(subset_sum([3,34,4,12,5,2],9))   
print(subset_sum([1,3,3],7))
