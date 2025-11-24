from typing import List, Tuple

def additions_score(lst1,lst2):
    l = len(lst1)
    count = 0
    for i in range(l):
        if int(lst2[i]) == sum(lst1[i]):
            count += 1
        else:
            break
    return count
        
print(additions_score([(1,2),(10,5),(7,8)], [3,15,16]))
print(additions_score([(2,2),(3,3)], [4,7,8]))
print( additions_score([], []))