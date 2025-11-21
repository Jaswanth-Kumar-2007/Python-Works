from typing import List

def partition(lst):
    p = lst[0]
    res = []
    if p < len(lst):
        for i in range(len(lst)):
            if i < p:
                res.append(lst[i])
    return res

print(partition([5,2,9,3,6,8]))
print(partition([3,3,3,3]))