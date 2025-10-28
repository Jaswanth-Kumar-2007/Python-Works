def nested_sum(lst,depth=1):
    sum = 0
    for i in lst:
        if type(i) == int or type(i) == float:
            sum += i*depth
        else:
            sum += nested_sum(i,depth+1)
    return sum

print(nested_sum([1,[4,[6]]]))
print(nested_sum([2,[3,[4,[5]]]]))