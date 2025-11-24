def chunk_list(lst,k):
    res = []
    if len(lst) == 0:
        return res
    elif k == 0:
        raise Exception("ValueError")
    while len(lst) > k:
        res.append(lst[0:k])
        lst = lst[k:]
    res.append(lst)
    return res

print(chunk_list([1], 0))
