def hcf_list(nums):
    
    common = {}
    for f in nums[0]:
        common[f] = common.get(f,0) + 1
        
    for lst in nums[1:]:
        common2 = {}
        for f2 in lst:
            common2[f2] = common2.get(f2,0) + 1
            
        new_common = {}
        for k in common2:
            if k in common:
                new_common[k] = min(common[k],common2[k])
        common = new_common
        
        hcf = []
        for key in common:
            for j in range(common[key]):
                hcf.append(key)
        return hcf
    
    

factor_lists = [
    [2,2,3,5],
    [2,2,5,7],
    [2,2,3,3,5,7,7]
]



print(hcf_list(factor_lists))
    