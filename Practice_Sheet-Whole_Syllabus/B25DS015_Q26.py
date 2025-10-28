def merge_sum(dict1,dict2):
    for j,k in dict2.items():
        if j in dict1:
            dict1[j] = dict1[j] + dict2[j]
        else:
            dict1[j] = k
    return dict1

print(merge_sum({'a':10,'b':5,'c':4}, {'b':7,'c':3}))