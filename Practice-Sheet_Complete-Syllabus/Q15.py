from typing import List

def partition(lst):
    p = lst[0]
    i = 1
    for j in range(1, len(lst)):
        if lst[j] <= p:
            lst[i], lst[j] = lst[j], lst[i]
            i += 1
    lst[0], lst[i-1] = lst[i-1], lst[0]
    return lst

lst = [5,2,3,6,8,9]
print(partition(lst))
