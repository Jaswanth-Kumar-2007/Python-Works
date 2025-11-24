from typing import List

def prime(n):
    if n == 0 or n == 1:
        return False
    elif n == 2:
        return True
    for i in range(n-1,1,-1):
        if n % i == 0:
            return False
    return True

def prime_factors(n):
    prime_lst = []
    res = []
    if n == 0 or n == 1:
        return res
    for i in range(2,n+1):
        if prime(i):
            prime_lst.append(i)
    if n in prime_lst:
        res.append(n)
        return res
    while n != 1:
        for i in prime_lst:
            if n%i == 0:
                res.append(i)
                n = n//i
    return sorted(res)

print(prime_factors(60))
print(prime_factors(23))
print(prime_factors(27))
            

