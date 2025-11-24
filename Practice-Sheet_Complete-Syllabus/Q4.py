def is_perfect(n):
    res = []
    for i in range(1,n):
        if n%i == 0:
            res.append(i)
    if sum(res) == int(n):
        return True
    else:
        return False

def perfect_up_to(limit):
    perfect_res = []
    for i in range(2,limit):
        if is_perfect(i):
            perfect_res.append(i)
    return perfect_res

print(perfect_up_to(1000))
