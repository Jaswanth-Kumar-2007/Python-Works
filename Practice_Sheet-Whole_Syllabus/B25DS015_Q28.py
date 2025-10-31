def longest_consecutive(nums):
    p = sorted(nums)
    res = []
    for i in p:
        res1 = []
        res1.append(i)
        n = i+1
        while n in p:
            res1.append(n)
            n = n+1
        res.append(res1)
        p.remove(i)
    
    f_res = {}
    for i in res:
        f_res[len(i)] = i
    s = max(f_res)

    return f_res[s]


print(longest_consecutive([100,4,200,1,2,3]))
print(longest_consecutive([0,3,7,2,5,8,4,6,0,1]))