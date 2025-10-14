"""
def factorial_check(num):
    for i in range(2,num+1):
        if  num % i == 0:
            while num % i != 0 :
                num = num // i
        if (num == 1):
            return True
    return False
"""

def factorial_check(num):
    for i in range(2, num + 1):          # start from 2
        if num % i == 0:                 # divide only if perfectly divisible
            while num % i == 0:          # keep dividing as long as possible
                num = num // i
        if num == 1:
            return True                  # if reduced to 1, it’s a factorial
    return False

#Cases = [1, 2, 6, 12,24,72, 120,13456,720, 5040, 40320, 362880, 3628800, 39916800, 479001600, 6227020800, 87178291200, 1307674368000, 20922789888000, 355687428096000, 6402373705728000, 121645100408832000]

#for i in Cases:
#   print(factorial_check(i))

print(factorial_check(720))      # might return True
print(factorial_check(5040))     # might return True
print(factorial_check(40320))    # might fail
print(factorial_check(24))
print(factorial_check(1000))       # probably fails

print(factorial_check(6))