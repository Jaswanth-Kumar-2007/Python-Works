def dictmaker(lst1,lst2):
    n = min(len(lst1),len(lst2))
    dic = {}
    for i in range(n):
        dic[lst1[i]] = lst2[i]
    return dic

lst1 = ["Apple","Banana","Cherry"]
lst2 = [32,36,24]
print(dictmaker(lst1,lst2))
