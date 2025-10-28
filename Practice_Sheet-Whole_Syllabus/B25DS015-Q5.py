def sum_digits(n):
    l = len(str(n))
    sum = 0
    for i in range(l):
        sum = sum + n%10
        n = n//10
    return sum

print(sum_digits(123))