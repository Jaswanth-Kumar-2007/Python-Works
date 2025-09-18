def movezeroestoend(arr):
    res = []
    count = 0
    for i in arr:
        if i != 0:
            res.append(i)
        else:
            count += 1
    for k in range(count):
        res.append(0)
    for i in range(len(arr)):
        arr[i] = res[i]

print(movezeroestoend([3,5,0,0,4]))
print(movezeroestoend([0,0]))
print(movezeroestoend([10,20,30]))