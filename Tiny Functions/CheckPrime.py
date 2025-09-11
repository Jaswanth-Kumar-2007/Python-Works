def checkprime(n):
   for i in range(n-1,1,-1):
        if (n%i == 0):
            return f"{n} is not Prime"
   return f"{n} is Prime"
        
print(checkprime(97))
print(checkprime(93))