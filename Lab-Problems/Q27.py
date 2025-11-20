def reverse_dictionary(d):
    res = {}
    for k,v in d.items():
        res[v] = k
    return res

print(reverse_dictionary({"one":"uno","two":"dos"}))
print(reverse_dictionary({}))
