def smart_sum(*args):
    '''
    Sum all numeric inputs, including numbers contained
    inside liststhemselves may be nested arbitrarily.
    Non-numeric values are notReturn the sum as an int or float.
    '''
    res = 0
    for arg in args:
        if type(arg) == int or type(arg) == float :
            res += arg
        elif type(arg) == list or type(arg) == tuple or type(arg) == set:
            res += smart_sum(*arg)
    return res

#Test Cases:
#print(smart_sum(1, 2, [3, 4], (5, 6)))
#print(smart_sum(10))
#print(smart_sum([1, [2, 3]])) 