def HCF_list(nums):
    res = []
    p = nums[0]
    for j in p:
        flag = True
        for lst in nums[1:]:
            if j not in lst:
                flag = False
                break
        if flag :
            res.append(j)
    t = 1
    for i in res:
        t = t*i
    return t,res
    

print(HCF_list([[2,2,3,5],[2,3,5,7],[2,2,3,3,5,5,11]]))
