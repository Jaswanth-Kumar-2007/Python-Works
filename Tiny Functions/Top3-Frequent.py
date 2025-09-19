def get_value(item):
    return item[1]



def Frequent_Items(nums):
    frequent = {}
    maxcount = 0
    for i in nums:
        count = 0
        for j in nums:
            if i == j:
                count += 1
        frequent[i] = count
    
    sorted_list = sorted(frequent.items(),key = get_value , reverse = True)
    res = []
    for item in sorted_list[:3]:
        res.append(item[0])
    
    return res

print(Frequent_Items([1,2,2,2,3,4,5,3,6,3,4,1,4,4,5,5,5]))
            
        
                