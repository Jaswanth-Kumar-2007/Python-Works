def decimal_binary(n):
    ans = 0
    i = 0
    while n > 0:               
        q = n % 2
        ans = ans + q * (10**i)
        n = n // 2              
        i += 1
    return ans

print(decimal_binary(7)) 
