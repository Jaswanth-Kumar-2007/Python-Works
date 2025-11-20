def remove_consecutive_duplicates(lst):
    res = []
    for i in range(len(lst)):
        j = i
        if i+1 < len(lst):
            while lst[i] == lst[j]:
                res.append(i)
                j = j + 1

    return lst

print(remove_consecutive_duplicates([1,1,2,2,2,3,1,1]))

