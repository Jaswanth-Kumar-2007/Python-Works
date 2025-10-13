def Fahren_to_Cels(lst):
    res = []
    for i in lst:
        res.append(((i*5)/9)+32)
    return res

nums = [18,45,90]
print(Fahren_to_Cels(nums))
