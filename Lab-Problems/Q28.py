def merge_with_priority(d1,d2):
    for k,v in d1.items():
        if k in d2:
            if d1[k] > d2[k]:
                d2[k] = d1[k]
        else:
            d2[k] = v
    return d2

print(merge_with_priority({"a":1,"b":2},{"b":20,"c":5}))
print(merge_with_priority({"x":3}, {}))
print(merge_with_priority({"x":3,"y":4},{"y":5,"z":6}))