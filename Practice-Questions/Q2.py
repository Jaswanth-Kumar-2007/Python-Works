test_dict = {"music":{"x":5,"y":6,"z":3},"best":{"x":8,"y":3,"z":5}}
res_dic = {}
for key , val in test_dict.items():
    lst = []
    for i,j in val.items():
        p = tuple(key,val[i])
        res_dic[i] = lst.append(p)

print(res_dic)