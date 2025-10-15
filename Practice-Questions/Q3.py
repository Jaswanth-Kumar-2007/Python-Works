# Write a program to compute value of  e^x which is accurate to 3 decimal place

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n*factorial(n-1)

def e_x(x):
    sum = 1
    for i in range(31):
        sum = float(float(sum) + (x^i)/factorial(i))
    return f"{sum:.3f}"

print(e_x(4))