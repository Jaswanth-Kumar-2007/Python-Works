def exp_taylor(x):
    terms=10
    result = 0
    factorial = 1
    power = 1
    for n in range(terms):
        result += power / factorial
        power *= x         # x^n
        factorial *= (n+1) # n!
    return result

print(exp_taylor(1))