def fib_generator(n):
    if n == 0:
        lst = []
        return lst
    elif n == 1:
        lst = [0]
        return lst
    lst = [0,1]
    while len(lst) != n:
        lst.append(lst[-2]+lst[-1])
    return lst

print(fib_generator(10))
print(fib_generator(1))
