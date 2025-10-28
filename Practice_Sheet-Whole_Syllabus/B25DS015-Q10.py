def flexible_sum(*args):
    if len(args) == 0:
        return 0
    sum = 0
    for i in args:
        sum += i
    return sum

print(flexible_sum())