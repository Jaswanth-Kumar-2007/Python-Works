def checkprime(n):
   for i in range(n-1,1,-1):
        if (n%i == 0):
            return False
   return True

def prime_factor(n):
    res_prime = []
    for i in range(2,n):
        if checkprime(i):
            res_prime.append(i)   
    res = []
    while n != 1:
        for r in res_prime:
            if n%r == 0:
                n = n/r
                res.append(r)
    return res

print(prime_factor(12))
                
            
        
    
                