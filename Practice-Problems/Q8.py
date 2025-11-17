def countnum(lst):
    dic = {}
    for i in lst:
        count = 0
        for j in lst:
            if i == j:
                count += 1
        dic[i] = count
    return dic


lst1 = [1,3,3,5,4,6,4,5,7,6,7,6,8,6,8]
for k,v in countnum(lst1).items():
    if v == 1:
        print(k)


        