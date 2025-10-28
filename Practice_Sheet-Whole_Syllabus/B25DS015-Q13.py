def find_intersection(set1,set2):
    res = set()
    for i in set1:
        if i in set2:
            res.add(i)
    return res

print(find_intersection({1,2,3,4},{2,4,5,6}))