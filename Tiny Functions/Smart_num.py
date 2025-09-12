def smart_sum(*args):
    res = 0
    for arg in args:
        if type(arg) == int or type(arg) == float :
            res += arg
        elif type(arg) == list or type(arg) == tuple or type(arg) == set:
            res += smart_sum(*arg)
    return res

print(smart_sum(1, 2, [3, 4], (5, 6)))
        
        
            