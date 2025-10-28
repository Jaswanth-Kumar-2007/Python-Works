def is_prime(n):
    if n == 1:
        return "This is Not Prime"
    for i in range(n-1,1,-1):
        if n % i == 0:
            return "This is Not Prime"
    return "This is Prime"

print(is_prime(9))
