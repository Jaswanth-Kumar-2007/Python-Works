from typing import List, Any

def eliminateDuplicates(ls):
    res = []
    for i in ls:
        if i not in res:
            res.append(i)
    return res

print(eliminateDuplicates([1,2,3,2,1]))
print(eliminateDuplicates(['a','b','a','c',]))