def remove_duplicates(items):
    res = []
    for i in items:
        if i not in res:
            res.append(i)
    return res

print(remove_duplicates([1,2,2,3,1,4]))