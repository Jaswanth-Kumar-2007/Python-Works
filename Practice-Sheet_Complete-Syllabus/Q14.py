from typing import List, Any

def merge(list1,list2):
    return sorted(list1+list2)

print(merge([1,3,5],[2,4,6]))
print(merge([],[1,2]))
print(merge([1,1,2],[1,2,2]))