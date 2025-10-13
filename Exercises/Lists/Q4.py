def Median(lst):
    dic = {}
    for i in lst:
        count = 0
        for j in lst:
            if int(i) == int(j):
                count += 1
        dic[i] = count
    s = max(dic.values())
    for k,val in dic.items():
        if dic[k] == s:
            return k
    
nums = [1,2,2,2,3,3,2,3,3,3,4,5]
print(Median(nums))