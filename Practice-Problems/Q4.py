def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
    
def sumfactorial(n):
    sum = 0
    for i in range(1,n):
        sum += factorial(i)*factorial(i+1)
    return sum

