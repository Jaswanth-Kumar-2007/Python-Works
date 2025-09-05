def calculate_factorial(n):
    #calculate the factorial of a non-negative integer n
    #Recursion Function
    #factorial of o and 1 is 1
    if (n == 0 or n == 1):
        return 1
    else:
        return n*calculate_factorial(n-1)
    

#TestCases:
#print(calculate_factorial(5))
#print(calculate_factorial(0))
#print(calculate_factorial(1))